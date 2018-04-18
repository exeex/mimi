from mimi import MidiFile, MidiTrack, generator
from mimi.instrument import Piano, Strings


tracks = [MidiTrack(channel=0, instrument=Piano.AcousticGrandPiano),
          MidiTrack(channel=1, instrument=Strings.Cello)]

for track in tracks:
    track.append_bar(generator.get_random_tab(tempo=70, key="C"))


mid = MidiFile()
mid.tracks.extend(tracks)
mid.draw_roll()
mid.play()
