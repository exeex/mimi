import unittest
import os
import mido
from mimi.Mimi import Note, Chord, Bar, Tab
from mimi import MidiTrack, MidiFile, Mode


# initialize


# New Bar in key C maj, Octave =4
bar = Bar([Note(2), Note(4, 1 / 8), Note(3), Note(4), Note(4, 1 / 8)], key="C", mode=Mode.major, octave=4)

# New Bar in key C maj, Octave =4, with Chord I maj
bar2 = Bar(
    [Chord(Note(0), Note(2), Note(4)), Note(0, 1 / 8), Note(2, 1 / 8), Chord(Note(0), Note(2), Note(4)), Note(0, 1 / 8),
     Note(2, 1 / 8)], key="C", mode=Mode.major, octave=4)


# Test bar

class MimiTest(unittest.TestCase):

    def test_bar(self):
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)

        # append bar to track
        track.append(bar)
        track.append(bar2)

        # save file
        # mid.save("test_bar.mid")


    def test_tab(self):

        mid = mido.MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)

        # append tab to track
        tab = Tab(bar, bar2, bar)
        tab.append(bar2)
        track.append(tab)
        # mid.save("test_tab.mid")


    def test_tab_to_array(self):

        tab = Tab(bar, bar2, bar)
        array = tab.to_array()

        return array

    def tearDown(self):

        return


if __name__ == '__main__':
    unittest.main()