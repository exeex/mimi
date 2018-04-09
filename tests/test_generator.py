from mimi import MidiFile, MidiTrack, output, generator
from mimi.instrument import *
import numpy as np
import os
from os.path import join
import unittest
import shutil
import matplotlib

class GeneratorTest(unittest.TestCase):

    def setUp(self):

        self.output_path = "output/"

        self.mid_path = join(self.output_path, "mid")
        self.json_path = join(self.output_path, "json")
        self.npy_path = join(self.output_path, "npy")
        self.wav_path = join(self.output_path, "wav")

        if not os.path.exists(self.output_path) :
            os.mkdir(self.output_path)

        if not os.path.exists(self.mid_path):
            os.mkdir(self.mid_path)

        if not os.path.exists(self.json_path):
            os.mkdir(self.json_path)

        if not os.path.exists(self.npy_path):
            os.mkdir(self.npy_path)

        if not os.path.exists(self.wav_path):
            os.mkdir(self.wav_path)

    def test_g(self):
        for x in range(10):
            # create midi object

            mid = MidiFile()
            track = MidiTrack(instrument=Guitar.AcousticGuitar_nylon)
            mid.tracks.append(track)

            # get random tab and append to midi track

            tab = generator.get_random_tab(tempo=70)
            filename = "%s" % str(x)
            track.append_bar(tab)

            # save files

            mid.save(join(self.mid_path, filename + ".mid"))

            array = tab.to_array()
            np.save(join(self.npy_path, filename + ".npy"), array)

            output.midi2wav(join(self.mid_path, filename + ".mid"), join(self.wav_path, filename + ".wav"))

            json = tab.to_json()
            output.json(join(self.json_path, filename + ".json"), json)


            # mid.draw_roll()

    def tearDown(self):
        shutil.rmtree(self.output_path)
if __name__ == '__main__':
    unittest.main()