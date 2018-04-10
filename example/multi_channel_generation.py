from mimi import MidiFile, MidiTrack, generator

tracks = [MidiTrack(channel=x,instrument=(x+1)*8) for x in range(3)]

for track in tracks:
    track.append_bar(generator.get_random_tab(tempo=70))

mid = MidiFile()
mid.tracks.extend(tracks)
mid.draw_roll()
mid.play()
