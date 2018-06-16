from mimi import MidiFile, MidiTrack, generator
from mimi.instrument import Piano,Organ,Guitar,Strings,Brass,SynthEffect,SynthLead
import os
import numpy as np

data_folder = "../data"
mp3_folder = "../data/mp3"
npz_folder = "../data/npz"
if not os.path.exists(data_folder):
    os.mkdir(data_folder)
if not os.path.exists(mp3_folder):
    os.mkdir(mp3_folder)
if not os.path.exists(npz_folder):
    os.mkdir(npz_folder)


for x in range(1):

    tracks = [MidiTrack(channel=0, instrument=Piano.AcousticGrandPiano),
              MidiTrack(channel=1, instrument=Guitar.ElectricGuitar_jazz),
              MidiTrack(channel=2, instrument=Strings.Cello),
              MidiTrack(channel=3, instrument=Brass.Trumpet),
              MidiTrack(channel=4, instrument=Organ.ChurchOrgan),
              MidiTrack(channel=5, instrument=Guitar.AcousticGuitar_steel),
              MidiTrack(channel=6, instrument=SynthLead.Lead2_sawtooth),
              MidiTrack(channel=7, instrument=Guitar.OverdrivenGuitar)]

    drum = MidiTrack(channel=9)

    choice = np.random.choice(8, 3, replace=False)
    tracks_ = [tracks[i] for i in choice]
    # tracks_.append(drum)

    for track in tracks_:
        track.append(generator.get_random_tab(tempo=70))

    mid = MidiFile()
    mid.tracks.extend(tracks_)
    # mid.draw_roll()

    # mid.save_mp3("data/mp3/%03d.mp3" % x)
    # mid.save_npz("data/npz/%03d.npz" % x)

    mid.play()
    print(tracks_)