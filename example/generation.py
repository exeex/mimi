from mimi import MidiFile, MidiTrack, output, generator
import numpy as np
import os
from os.path import join
import matplotlib

output_path = "output/"

mid_path = join(output_path, "mid")
json_path = join(output_path, "json")
npy_path = join(output_path, "npy")
wav_path = join(output_path, "wav")

if os.path.exists(output_path) is not True:
    os.mkdir(output_path)

if os.path.exists(mid_path) is not True:
    os.mkdir(mid_path)

if os.path.exists(json_path) is not True:
    os.mkdir(json_path)

if os.path.exists(npy_path) is not True:
    os.mkdir(npy_path)

if os.path.exists(wav_path) is not True:
    os.mkdir(wav_path)


for x in range(10):

    # create midi object

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # get random tab and append to midi track

    tab = generator.get_random_tab(tempo=70)
    filename = "%s" % str(x)
    track.append_bar(tab)


    # save files

    mid.save(join(mid_path, filename + ".mid"))

    array = tab.to_array()
    np.save(join(npy_path, filename + ".npy"), array)

    output.midi2wav(join(mid_path, filename + ".mid"),join(wav_path, filename + ".wav"))

    json = tab.to_json()
    output.json(join(json_path, filename + ".json"), json)


    # mid.draw_roll()
