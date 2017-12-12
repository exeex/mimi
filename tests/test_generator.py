import unittest
import generator as migen
from mido import MidiFile
from Mimi import MidiTrack
import numpy as np
import Output
import os


class GeneratorTest:


    path = "../output/"

    for x in range(1):
        tab = migen.get_random_tab(tempo=70)
        filename = "gggg"

        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
        track.append_bar(tab)

        mid.save(os.path.join(path,"mid",filename+".mid"))

        array = tab.to_array()
        np.save(os.path.join(path,"npy",filename+".npy"), array)

        Output.midi2mp3(os.path.join(path,"mid",filename+".mid"), os.path.join(path,"wav",filename+".wav"))

        json = tab.to_json()
        Output.json(os.path.join(path,"json",filename+".json"), json)

        Output.play(os.path.join(path,"mid",filename+".mid"))