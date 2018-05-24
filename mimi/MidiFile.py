import mido
import numpy as np
import os
import platform
from mimi.instrument import *
from mido import Message

module_root_path = os.path.split(os.path.abspath(__file__))[0]  # mimi/
cfg_file = os.path.join(module_root_path, "soundfont", "soundfont.cfg")  # mimi/soundfont/soundfont.cfg
sf2_folder = os.path.join(module_root_path, "soundfont")  # mimi/soundfont/
default_sf2 = "8MBGMSFX.SF2"  # 8MBGMSFX.SF2


def set_soundfont(dir=None):
    if dir is None:
        with open(cfg_file, 'w') as f:
            f.write("dir {} \nsoundfont \"{}\" amp=200%".format(sf2_folder, default_sf2))
    else:
        with open(cfg_file, 'w') as f:

            folder = os.path.split(dir)[0]
            sf2 = os.path.split(dir)[1]
            f.write("dir {} \nsoundfont \"{}\" amp=200%".format(folder, sf2))


class MidiFile(mido.MidiFile):

    def __init__(self, filename=None):

        mido.MidiFile.__init__(self, filename)

        self.meta = {}
        # assume only 0 or 1 program change event in each channel
        # default instrument is Piano in ch.0

        if filename is not None:
            for idx, track in enumerate(self.tracks):
                # remove mido.UnknownMetaMessage in track (which would cause error)
                self.tracks[idx] = [msg for msg in track if not isinstance(msg, mido.UnknownMetaMessage)]

        self.instrument = [-1 for x in range(16)]
        self.instrument[0] = 1

    def __add__(self, other):

        ret = MidiFile()
        ret.tracks.append(self.tracks)
        ret.tracks.append(other.tracks)

        return ret

    def get_events(self):

        """

        > "midi event" is equal to "message"
        > "tracks" is almost equal to "channel"

        :return: list[channel][event_nb]
        return a list of events in different channel
        """

        # There is > 16 channel in midi.tracks. However there is only 16 channel related to "music" events.
        # We store music events of 16 channel in the list "events" with form [[ch1],[ch2]....[ch16]]
        # Lyrics and meta data used a extra channel which is not include in "events"

        events = [[] for _ in range(16)]

        # Iterate all event in the midi and extract to 16 channel form

        for track in self.tracks:
            for msg in track:
                try:
                    channel = msg.channel
                    events[channel].append(msg)

                # if a msg has no channel
                except AttributeError:
                    if isinstance(msg, mido.MetaMessage):
                        print(msg)
                    continue

        return events

    def get_instrument(self):

        events = self.get_events()

        # Now we just assume there is only 1 program change in each channel

        for idx_channel, channel in enumerate(events):
            for msg in channel:
                if msg.type == "program_change":
                    self.instrument[idx_channel] = msg.program
                    # print("program_change", " channel:", idx_channel, "pc")
        return self.instrument

    def get_events_from_roll(self, roll: np.ndarray):

        chan, pitch, tick = roll.shape

        if chan != 16:
            raise IndexError
        if pitch != 128:
            raise IndexError

        tracks = [self._get_events_from_roll(roll[i, :, :], i) for i in range(16)]

        return tracks

    def _get_events_from_roll(self, chan: np.ndarray, chan_idx):

        chan = (chan > 0) * 1  # binarize
        chan = np.pad(chan, [[0, 0], [1, 0]], mode='constant', constant_values=[0, 0])
        diff = np.diff(chan, axis=1)  # TODO: pad zero left
        on_set = diff > 0
        off_set = diff < 0

        on_set_indices = np.where(on_set)
        on_set_indices = [(on_set_indices[0][i], on_set_indices[1][i], 'on') for i in range(len(on_set_indices[0]))]

        off_set_indices = np.where(off_set)
        off_set_indices = [(off_set_indices[0][i], off_set_indices[1][i], 'off') for i in range(len(off_set_indices[0]))]

        # TODO: fix events
        events = sorted(off_set_indices + on_set_indices, key=lambda x: x[1])
        print(events)

        # self.append(Message('note_off', note=object.pitch, velocity=64, time=object.time, channel=self.channel))

        try:
            time_intervals = [events[0][1]] + [events[i + 1][1] - events[i][1] for i in range(len(events) - 1)]
            # print(time_intervals)
        except IndexError:
            print(events)
            return []

        track = []
        for idx, event in enumerate(events):
            if event[2] == 'on':
                # TODO: velocity & volume
                track.append(Message('note_on', note=event[0], velocity=64,
                                     time=time_intervals[idx], channel=chan_idx))

            if event[2] == 'off':
                # TODO: velocity & volume
                track.append(Message('note_off', note=event[0], velocity=64,
                                     time=time_intervals[idx], channel=chan_idx))

        # pitch, ticks = diff.shape

        # for x in range(ticks):

        return track

    def get_roll(self, down_sample_rate=10):
        events = self.get_events()
        # Identify events, then translate to piano roll
        # choose a sample ratio(sr) to down-sample through time axis
        sr = down_sample_rate

        # compute total length in tick unit
        length = self.get_total_ticks()

        # allocate memory to numpy array
        roll = np.zeros((16, 128, length // sr), dtype="int8")

        # use a register array to save the state(no/off) for each key
        note_register = [int(-1) for _ in range(128)]

        for idx_channel, channel in enumerate(events):

            time_counter = 0
            volume = 100
            # Volume would change by control change event (cc) cc7 & cc11
            # Volume 0-100 is mapped to 0-127

            print("channel", idx_channel, "start")
            for msg in channel:
                if msg.type == "control_change":
                    if msg.control == 7:
                        volume = msg.value
                        # directly assign volume
                    if msg.control == 11:
                        volume = volume * msg.value // 127
                        # change volume by percentage
                        # print("cc", msg.control, msg.value, "duration", msg.time)

                if msg.type == "program_change":
                    self.instrument[idx_channel] = msg.program
                    print("program_change", " channel:", idx_channel, "pc", msg.program, "time", time_counter,
                          "duration", msg.time)

                if msg.type == "note_on":
                    print("\t note on ", msg.note, "time", time_counter, "duration", msg.time, "velocity", msg.velocity)
                    note_on_start_time = time_counter // sr
                    note_on_end_time = (time_counter + msg.time) // sr
                    intensity = volume * msg.velocity // 127

                    # When a note_on event *ends* the note start to be play
                    # Record end time of note_on event if there is no value in register
                    # When note_off event happens, we fill in the color
                    if note_register[msg.note] == -1:
                        note_register[msg.note] = (note_on_end_time, intensity)
                    else:
                        # When note_on event happens again, we also fill in the color
                        old_end_time = note_register[msg.note][0]
                        old_intensity = note_register[msg.note][1]
                        roll[idx_channel, msg.note, old_end_time: note_on_end_time] = old_intensity
                        note_register[msg.note] = (note_on_end_time, intensity)

                if msg.type == "note_off":
                    print("\t note off", msg.note, "time", time_counter, "duration", msg.time, "velocity", msg.velocity)
                    note_off_start_time = time_counter // sr
                    note_off_end_time = (time_counter + msg.time) // sr
                    note_on_end_time = note_register[msg.note][0]
                    intensity = note_register[msg.note][1]
                    # fill in color
                    roll[idx_channel, msg.note, note_on_end_time:note_off_end_time] = intensity

                    note_register[msg.note] = -1  # reinitialize register

                time_counter += msg.time

                # TODO: velocity -> done, but not verified
                # TODO: Pitch wheel
                # TODO: Channel - > Program Changed / Timbre catagory
                # TODO: real time scale of roll

            # if there is a note not closed at the end of a channel, close it
            for key, data in enumerate(note_register):
                if data != -1:
                    note_on_end_time = data[0]
                    intensity = data[1]
                    # print(key, note_on_end_time)
                    note_off_start_time = time_counter // sr
                    roll[idx_channel, key, note_on_end_time:] = intensity
                note_register[idx_channel] = -1

            print("channel", idx_channel, "end")

        return roll

    def draw_roll(self, color_bar=False):

        try:
            import matplotlib.pyplot as plt
            import matplotlib as mpl
            from matplotlib.colors import colorConverter
        except ImportError:
            raise ImportError('You need to install matplotlib. (pip install matplotlib)')
        sr = 10
        roll = self.get_roll(down_sample_rate=sr)

        # build and set fig obj
        plt.ioff()
        fig = plt.figure(figsize=(4, 3))
        a1 = fig.add_subplot(111)
        a1.axis("equal")
        a1.set_facecolor("black")

        # change unit of time axis from tick to second
        tick = self.get_total_ticks()
        second = mido.tick2second(tick, self.ticks_per_beat, self.get_tempo())
        print("midi length: ", second, "sec")
        if second > 10:
            x_label_period_sec = second // 10
        else:
            x_label_period_sec = second / 10  # ms
        # print(x_label_period_sec)
        x_label_interval = mido.second2tick(x_label_period_sec, self.ticks_per_beat, self.get_tempo()) / sr
        # print(x_label_interval)
        plt.xticks([int(x * x_label_interval) for x in range(20)],
                   [round(x * x_label_period_sec, 2) for x in range(20)])

        # change scale and label of y axis
        plt.yticks([y * 16 for y in range(8)], [y * 16 for y in range(8)])

        # build colors for different channel
        channel_nb = 16
        transparent = colorConverter.to_rgba('black')
        colors = [mpl.colors.to_rgba(mpl.colors.hsv_to_rgb((i / channel_nb, 1, 1)), alpha=1) for i in range(channel_nb)]
        cmaps = [mpl.colors.LinearSegmentedColormap.from_list('my_cmap', [transparent, colors[i]], 128) for i in
                 range(channel_nb)]

        # build color maps
        for i in range(channel_nb):
            cmaps[i]._init()
            # create your alpha array and fill the colormap with them.
            alphas = np.linspace(0, 1, cmaps[i].N + 3)
            # create the _lut array, with rgba values
            cmaps[i]._lut[:, -1] = alphas

        # draw piano roll and stack image on a1
        for i in range(channel_nb):
            try:
                a1.imshow(roll[i], origin="lower", interpolation='nearest', aspect='auto', cmap=cmaps[i])
            except IndexError:
                pass

        # draw color bar
        if color_bar:
            colors = [mpl.colors.hsv_to_rgb((i / channel_nb, 1, 1)) for i in range(channel_nb)]
            cmap = mpl.colors.LinearSegmentedColormap.from_list('my_cmap', colors, 16)
            a2 = fig.add_axes([0.05, 0.80, 0.9, 0.15])
            cbar = mpl.colorbar.ColorbarBase(a2, cmap=cmap,
                                             orientation='horizontal',
                                             ticks=list(range(16)))

        # show piano roll
        plt.draw()
        plt.ion()
        plt.show(block=True)

    def get_seconds(self):
        tick = self.get_total_ticks()
        return mido.tick2second(tick, self.ticks_per_beat, self.get_tempo())

    def get_tempo(self):
        try:
            return self.meta["set_tempo"]["tempo"]
        except:
            return 500000

    def get_total_ticks(self):

        events = self.get_events()
        max_ticks = 0
        for channel in range(16):
            ticks = sum(msg.time for msg in events[channel])
            if ticks > max_ticks:
                max_ticks = ticks
        return max_ticks

    def save_npz(self, filename=None):
        array = self.get_roll()
        instrument = np.array(self.get_instrument())
        np.savez(filename, data=array, instrument=instrument)

    def save_png(self, filename=""):
        try:
            import scipy.misc
        except ImportError:
            raise ImportError("You need to install scipy.")
        array = self.get_roll()

        track_nb = len(self.tracks)

        for idx in range(track_nb):
            scipy.misc.toimage(array[idx, :, :], cmin=0.0).save('%s%d.png' % (filename, idx))

    def save_mp3(self, filename="out.mp3"):
        tmp_file = "%s_tmp.mid" % filename
        self.save(tmp_file)
        module_root_path = os.path.split(os.path.abspath(__file__))[0]

        total_time = self.get_seconds()

        # set cfg_file to mimi/soundfont/8MBGMSFX.cfg
        cfg_file = os.path.join(module_root_path, "soundfont", "8MBGMSFX.cfg")

        _platform = platform.system()
        if _platform == "linux" or _platform == "linux2" or _platform == "Linux":
            # use -map_channel 0.0.0 to map left channel to mono tone mp3 file
            os.system(
                "timidity -c %s %s -Ow -o - | ffmpeg -t %f -i - -acodec libmp3lame -ab 256k -map_channel 0.0.0 %s" %
                (cfg_file, tmp_file, total_time, filename))
        else:
            os.system("timidity -c %s %s -Ow -o - | ffmpeg -t %f -i - -acodec libmp3lame -ab 256k %s" %
                      (cfg_file, tmp_file, total_time, filename))

        os.remove(tmp_file)

        # TODO: save tmp_file in tmp_folder

    def play(self, filename="tmp"):

        tmp_file = "%s_tmp.mid" % filename
        self.save(tmp_file)

        _platform = platform.system()
        if _platform == "linux" or _platform == "linux2" or _platform == "Linux":
            # use -map_channel 0.0.0 to map left channel to mono tone mp3 file
            os.system("timidity -c %s %s -Ow -o - | ffmpeg -i - -map_channel 0.0.0 -f wav - | ffplay -i -" % (
                cfg_file, tmp_file))
        else:
            os.system("timidity -c %s %s -A100" % (cfg_file, tmp_file))

        os.remove(tmp_file)

        # TODO: save tmp_file in tmp_folder


set_soundfont()

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import scipy.signal

    mid = MidiFile("test_file/imagine_dragons-believer.mid")
    plt.axis('equal')
    r = mid.get_roll(10)
    # tracks = mid.get_events_from_roll(r)

    l = r[:, :, 3000:6000]
    plt.imshow(l[3,:,:], origin="lower", interpolation='nearest', aspect='auto')
    plt.show()

    l2 = mid.get_events_from_roll(l)

    mid2 = MidiFile()
    mid2.tracks.extend(l2)
    l3 = mid2.get_roll()
    plt.imshow(l3[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
    plt.show()

    # get the list of all events
    # events = mid.get_events()
    # get the np array of piano roll image
    # roll = mid.get_roll()

    # draw piano roll by pyplot
    # mid.draw_roll()
    # mid.save_npz("gg")

    # set_soundfont(r"C:\Users\cswu\Desktop\mimi\mimi\soundfont\FluidR3_GM.sf2")
    # mid.play()
    # mid.save_mp3()
