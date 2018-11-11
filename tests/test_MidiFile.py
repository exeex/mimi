from mimi import MidiFile
import unittest
import matplotlib.pyplot as plt
import numpy as np
import os
from mimi import MidiFile, MidiTrack, generator
from mimi.instrument import Piano, Organ, Guitar, Strings, Brass, SynthEffect, SynthLead

import tempfile

class TestMidiFile(unittest.TestCase):

    def setUp(self):
        self.mid = MidiFile("../mimi/test_file/imagine_dragons-believer.mid")
        self.roll = self.mid.get_roll()
        self.test_roll = self.roll[:, :, 3000:6000]

    def test__get_events_from_roll(self):
        # plt.imshow(self.test_roll[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        # plt.show()

        track = self.mid._get_events_from_roll(self.test_roll[3, :, :], 3)

        mid2 = MidiFile()
        mid2.tracks.append(track)

        roll = mid2.get_roll(down_sample_rate=1)[3, :, :]
        # plt.imshow(roll, origin="lower", interpolation='nearest', aspect='auto')
        # plt.show()

        diff = ((roll > 0) * 1 - (self.test_roll[3, :, :roll.shape[1]] > 0) * 1)
        diff2 = roll - self.test_roll[3, :, :roll.shape[1]]

        ret1 = diff.sum()
        if ret1 != 0:
            raise ValueError

        ret2 = (diff2.sum())
        if ret2 != 0:
            raise ValueError

    def test_get_events_from_roll(self):
        # plt.imshow(self.test_roll[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        # plt.show()
        # plt.close()

        l2 = self.mid.get_events_from_roll(self.test_roll)

        mid2 = MidiFile()
        mid2.tracks.extend(l2)
        l3 = mid2.get_roll()
        # plt.imshow(l3[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        # plt.show()
        #
        # plt.close()

    def test_key_shift(self):

        for x in range(1):

            tracks = [MidiTrack(channel=0, instrument=Piano.AcousticGrandPiano),
                      MidiTrack(channel=1, instrument=Guitar.ElectricGuitar_jazz),
                      MidiTrack(channel=2, instrument=Strings.Cello),
                      MidiTrack(channel=3, instrument=Brass.Trumpet),
                      MidiTrack(channel=4, instrument=Organ.ChurchOrgan),
                      MidiTrack(channel=5, instrument=Guitar.AcousticGuitar_steel),
                      MidiTrack(channel=6, instrument=SynthLead.Lead2_sawtooth),
                      MidiTrack(channel=7, instrument=Guitar.OverdrivenGuitar)]


            tracks_ = [tracks[i] for i in [1,2,3]]

            for track in tracks_:
                track.append(generator.get_random_tab(tempo=70))

            combo = ["123"]

            mid_ = MidiFile()
            mid_.tracks.extend(tracks_)
            mid_.set_tick_per_beat(50)

            for indices in combo:
                mid = MidiFile()
                mid.set_tick_per_beat(50, resample=False)

                for index in indices:
                    mid.tracks.append(tracks_[int(index) - 1])
                # TODO : fix 1+2+3 bug
                # TODO : resample bug
                # TODO : only piano bug

                event_nb = []
                for key_shift in range(3):
                    mid.key_shift(1)
                    print(len(mid.get_events()[0]))
                    event_nb.append(len(mid.get_events()[0]))


                if event_nb[0]!=event_nb[1]:
                    raise ValueError






    def test_save_npz(self):

        self.mid.save_npz("test.npz")
        os.remove('test.npz')


    def test_save_mp3(self):

        mid = self.mid
        directory_name = tempfile.mkdtemp()
        mp3_path = os.path.join(directory_name,'test.mp3')
        mid.save_mp3(mp3_path)
        # os.remove(mp3_path)
        # os.removedirs(directory_name)

        print(directory_name)

    def test_play(self):
        # set_soundfont(r"C:\Users\cswu\Desktop\mimi\mimi\soundfont\FluidR3_GM.sf2")
        self.mid.play()



    def test_get_roll(self):
        mid = self.mid
        roll = mid.get_roll()
        l = roll[:, :, 3000:6000]
        # plt.imshow(l[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        # plt.show()
        mid.draw_roll()

    def tearDown(self):

        del self.mid
        del self.roll
        del self.test_roll
        return 0
