from mimi import MidiFile
import unittest
import matplotlib.pyplot as plt
import numpy as np
import os


class TestMidiFile(unittest.TestCase):

    def setUp(self):
        self.mid = MidiFile("../mimi/test_file/imagine_dragons-believer.mid")
        self.roll = self.mid.get_roll(10)
        self.test_roll = self.roll[:, :, 3000:6000]

    def test__get_events_from_roll(self):
        plt.imshow(self.test_roll[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        # plt.show()

        track = self.mid._get_events_from_roll(self.test_roll[3, :, :], 3)

        mid2 = MidiFile()
        mid2.tracks.append(track)

        roll = mid2.get_roll(down_sample_rate=1)[3, :, :]
        plt.imshow(roll, origin="lower", interpolation='nearest', aspect='auto')
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
        plt.imshow(self.test_roll[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        # plt.show()

        l2 = self.mid.get_events_from_roll(self.test_roll)

        mid2 = MidiFile()
        mid2.tracks.extend(l2)
        l3 = mid2.get_roll()
        plt.imshow(l3[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        # plt.show()

    def test_save_npz(self):

        self.mid.save_npz("test.npz")
        os.remove('test.npz')


    def test_save_mp3(self):

        mid = self.mid
        plt.axis('equal')
        mid.save_mp3('test.mp3')
        os.remove('test.mp3')

    def test_play(self):
        # set_soundfont(r"C:\Users\cswu\Desktop\mimi\mimi\soundfont\FluidR3_GM.sf2")
        self.mid.play()



    def test_get_roll(self):
        mid = self.mid
        events = mid.get_events()
        roll = mid.get_roll()
        l = roll[:, :, 3000:6000]
        plt.imshow(l[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        plt.show()
        mid.draw_roll()

    def tearDown(self):

        del self.mid
        del self.roll
        del self.test_roll
        return 0
