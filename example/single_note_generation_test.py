from mimi import MidiFile, MidiTrack, generator
from mimi.Mimi import AbsNote
from mimi.instrument import Piano, Strings




track = MidiTrack(channel=0, instrument=Piano.AcousticGrandPiano)


for x in range(40, 76):
    track.append(AbsNote(pitch=x,time=256))

# 把track放到MidiFile物件中
mid = MidiFile()
mid.tracks.append(track)

# 對mid物件進行存檔/播放等操作
mid.save_mp3("test.mp3")
