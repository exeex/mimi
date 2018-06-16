import random
import numpy as np
from mimi import MidiTrack, MidiFile
from mimi.Mimi import Note, Bar, Chord, Tab
from mimi.Mode import major, minor, key_dict
from mimi.output import midi2wav,json,play
from mimi.instrument import Piano


def get_random_note(pitch=None, time=None):
    if pitch is None:
        pitch = random.randint(0, 7)
    if time is None:
        note_type = random.randint(0, 3)
        time_list = [1 / 2, 1 / 4, 1 / 8, 1 / 16]
        time = time_list[note_type]

    return Note(pitch, time)


def get_random_chord(pitch=None, time=None):
    if pitch is None:
        pitch = random.randint(0, 7)

    if time is None:
        note_type = random.randint(0, 3)
        time_list = [1 / 2, 1 / 4, 1 / 8, 1 / 16]
        time = time_list[note_type]

    return Chord(Note(pitch, time), Note(pitch + 2, time), Note(pitch + 4, time))


def get_random_note_chord():
    if random.randint(0, 2) == 0:
        return get_random_chord()
    else:
        return get_random_note()


def check_bar(bar: Bar):
    unit_note_time = 1 / bar.time_sign[1]
    note_per_bar = bar.time_sign[0]
    max_time = unit_note_time * note_per_bar

    total_time = 0.
    for note in bar.notes:
        total_time += note.time

    if total_time > max_time:
        redundant_time = total_time - max_time
        return redundant_time

    else:
        return True

        # TODO: time_signature check
        # TODO: support chord


def get_random_tab(key=None, mode=None, octave=None, tempo=None):
    if key is None:
        keys = list(key_dict.keys())
        key_nb = len(keys)
        random_key_index = random.randint(0, key_nb - 1)
        key = keys[random_key_index]
    print(key)

    if mode is None:
        i = random.randint(0, 1)

        if i is 0:
            mode = major
        else:
            mode = minor
    print(i, mode)

    if octave is None:
        octave = random.randint(3, 5)
    print(octave)

    if tempo is None:
        tempo = random.randint(60, 120)
    print(tempo)

    tab = Tab()

    for x in range(8):

        bar = Bar(key=key, mode=mode, octave=octave, tempo=tempo)

        while check_bar(bar) is True:
            bar.append(get_random_note_chord())

        redundant_time = check_bar(bar)
        last_note = bar.pop()
        last_note.time = last_note.time - redundant_time
        if last_note.time != 0.:
            bar.append(last_note)

        tab.append(bar)

    return tab


if __name__ == "__main__":
    for x in range(1):
        tab = get_random_tab(tempo=120)
        filename = "ElectricPiano1"

        mid = MidiFile()
        track = MidiTrack(instrument=Piano.ElectricPiano1)
        mid.tracks.append(track)
        track.append(tab)

        # mid.save("./mid/%s.mid" % filename)
        #
        # array = tab.to_array()
        # np.save("./npy/%s.npy" % filename, array)
        #
        # midi2wav("./mid/%s.mid" % filename, "./wav/%s.wav" % filename)
        #
        # json = tab.to_json()
        # json("./json/%s.mid" % filename, json)
        #
        # play("./%s.mid" % filename)

        mid.play()
