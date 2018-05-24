from mimi import MidiFile
import unittest
import matplotlib.pyplot as plt
import numpy as np

class TestMidiFile(unittest.TestCase):



    def setUp(self):

        self.mid = MidiFile("../mimi/test_file/imagine_dragons-believer.mid")
        self.roll = self.mid.get_roll(10)
        self.test_roll = self.roll[:, :, 3000:6000]


    def test__get_events_from_roll(self):
        plt.imshow(self.test_roll[3,:,:], origin="lower", interpolation='nearest', aspect='auto')
        plt.show()

        track = self.mid._get_events_from_roll(self.test_roll[3,:,:], 3)

        mid2 = MidiFile()
        mid2.tracks.append(track)

        roll = mid2.get_roll(down_sample_rate=1)[3, :, :]
        plt.imshow(roll, origin="lower", interpolation='nearest', aspect='auto')
        plt.show()

        diff = ((roll > 0) *1 - (self.test_roll[3,:,:roll.shape[1]] > 0)*1)


        print(diff.sum())


    def test_get_events_from_roll(self):


        plt.imshow(self.test_roll[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        plt.show()

        l2 = self.mid.get_events_from_roll(self.test_roll)

        mid2 = MidiFile()
        mid2.tracks.extend(l2)
        l3 = mid2.get_roll()
        plt.imshow(l3[3, :, :], origin="lower", interpolation='nearest', aspect='auto')
        plt.show()

    def tearDown(self):
        pass