import mido
from mido import Message
from mimi.instrument import Piano
from mimi.Mimi import Note, AbsNote, Chord, Bar, Tab
from typing import Union


class MidiTrack(mido.MidiTrack):

    def __init__(self, channel=0, instrument=Piano.AcousticGrandPiano):
        super(MidiTrack, self).__init__()
        self.__append = super(MidiTrack, self).append
        self.instrument = instrument
        self.channel = channel
        self.append(Message('program_change', program=instrument, time=0, channel=self.channel))

    def append(self, object: Union[AbsNote, Message, Bar, Tab, list, Chord], overwrite_instrument=False):
        """
        append music element to the track
        input type could be:

        * AbsNote : 一個音符，pitch以midi-128音階定義，時間長度為midi的時間長度
        * Message : midi messsage
        * Bar : 一個bar是一個小節
        * Tab : 一個tab是數個bar組成

        :param object: the music element to be appended
        :return:
        """
        if type(object) is Message:
            self.__append(object)

        elif type(object) is AbsNote:
            self.append(Message('note_on', note=object.pitch, velocity=64, time=0, channel=self.channel))
            self.append(Message('note_off', note=object.pitch, velocity=64, time=object.time, channel=self.channel))

        elif type(object) is Bar:
            self.__append_bar(object)

        elif type(object) is Chord:
            self.__append_chord(object)

        elif type(object) is Tab:
            for bar in object.bars:
                self.__append_bar(bar)

        # dirty midi msg list
        elif type(object) is list:
            self.__append_list(object, overwrite_instrument=overwrite_instrument)

    def __append_chord(self, chord: Chord):

        pitch = 0
        time = 0
        # print("chord: ", chord)

        for chord_note in chord.chord:
            pitch = chord_note.pitch
            time = chord_note.time
            self.append(Message('note_on', note=pitch, velocity=64, time=0, channel=self.channel))

        self.append(Message('note_off', note=pitch, velocity=64, time=time, channel=self.channel))

        for chord_note in reversed(chord.chord[:-1]):
            pitch = chord_note.pitch
            self.append(Message('note_off', note=pitch, velocity=64, time=0, channel=self.channel))

    def __append_bar(self, bar: Bar):
        for note in bar.notes:

            if type(note) is Note:

                pitch = bar.to_128_pitch(note)
                time = bar.to_time(note)
                print(pitch, time, note)

                self.append(Message('note_on', note=pitch, velocity=64, time=0, channel=self.channel))
                self.append(Message('note_off', note=pitch, velocity=64, time=time, channel=self.channel))

            elif type(note) is Chord:

                pitch = 0
                time = bar.to_time(note)
                print("chord: ", time, note)

                for chord_note in note.chord:
                    pitch = bar.to_128_pitch(chord_note)
                    self.append(Message('note_on', note=pitch, velocity=64, time=0, channel=self.channel))

                self.append(Message('note_off', note=pitch, velocity=64, time=time, channel=self.channel))

                for chord_note in reversed(note.chord[:-1]):
                    pitch = bar.to_128_pitch(chord_note)
                    self.append(Message('note_off', note=pitch, velocity=64, time=0, channel=self.channel))

            # TODO: Volume control
            # TODO: time shift
            # TODO: independent end time for notes in chord
            # TODO: Program change ---> done, ready to be tested

        return

    def __check_channel_consistent(self, l):

        channel = None

        for idx, msg in enumerate(l):

            if channel is None:
                try:
                    channel = msg.channel
                    # time = msg.time
                    # mtype = msg.type
                    # print(mtype, channel, time)
                except AttributeError:
                    print(msg.type)
            else:
                try:
                    _channel = msg.channel
                    # time = msg.time
                    # type = msg.type
                    # print(type, channel, time)

                    if channel != _channel:
                        raise ValueError("the track is invalid, channel didn't consistent in track. msg idx = %d: %s"
                                         % (idx, msg))

                except AttributeError:
                    print(msg.type)
        return True

    def set_instrument(self, ins_nb):
        self.instrument = ins_nb
        pc_event = self.__getitem__(0)
        pc_event.program = ins_nb

    def __append_list(self, l, overwrite_instrument=False):

        if self.__check_channel_consistent(l):
            for idx, msg in enumerate(l):

                if msg.type == "note_on":
                    msg = msg.copy()
                    msg.channel = self.channel
                    self.append(msg)
                elif msg.type == "note_off":
                    msg = msg.copy()
                    msg.channel = self.channel
                    self.append(msg)
                elif msg.type == "end_of_track":
                    msg = msg.copy()
                    self.append(msg)
                elif msg.type == "program_change":
                    if overwrite_instrument:
                        self.set_instrument(msg.program)
                    time = msg.time
                    # Place holder event
                    self.append(Message('control_change', control=15, value=0, time=time))
                else:
                    try:
                        time = msg.time
                        # print(time)
                        # Place holder event
                        self.append(Message('control_change', control=15, value=0, time=time))
                    except AttributeError as e:
                        print(e)

                # TODO: merge place holder events


if __name__ == "__main__":
    from mimi.MidiFile import MidiFile
    #
    # t = MidiTrack(instrument=44)
    # mid = gg.MidiFile("./test_file/imagine_dragons-believer.mid")
    # t.append(mid.tracks[5])
    # t.set_instrument(56)
    # mid2 = gg.MidiFile()
    # mid2.tracks.append(t)
    # mid2.play()

    with MidiFile() as mid:
        track = MidiTrack(channel=0, instrument=0)
        track.append(Chord(*[AbsNote(pitch=x, time=30000) for x in range(39, 97)]))
        mid.tracks.append(track)
        # mid.save_mp3("data/mp3/%03d-%03d.mp3" % (ins, x))
        # mid.save_npz("data/npz/%03d-%03d.npz" % (ins, x))
        # print(Chord(*[AbsNote(pitch=x, time=256) for x in range(39, 97)]))

        mid.play()
        # print(mid.get_seconds())