from mimi import MidiFile, MidiTrack, generator
from mimi.instrument import Piano, Strings

"""

# 物件結構

MidiFile > MidiTrack > Message

## MidiFile

MidiFile是讀進來的mid檔案物件

## MidiTrack

MidiTrack是MidiFile中的音軌物件
MidiFile取出track:
```m = MidiFile("test.mid")```
```m.tracks[0]                   #0號track```

## Message

Message是midi事件(包含指定樂器、指定頻道、彈奏指定音符、音量調整等)
MidiTrack取出Message：
```t = MidiTrack(channel=0)```
```t[0]                          #0號Message```


# channel vs track

* channel最多只有16個，track不限
* 你可以有複數個track放在同一個channel #但不建議
* 一個channel只配一種樂器，配兩種會有bug

#

"""


# 創造兩個track，放在不同channel，使用不同樂器
tracks = [MidiTrack(channel=0, instrument=Piano.AcousticGrandPiano),
          MidiTrack(channel=1, instrument=Strings.Cello)]

# 對每個track生成隨機音符/和弦
for track in tracks:
    track.append_bar(generator.get_random_tab(tempo=70, key="C"))

# 把tracks放到MidiFile物件中
mid = MidiFile()
mid.tracks.extend(tracks)

# 對mid物件進行存檔/播放等操作
mid.draw_roll()
mid.play()
# roll = mid.get_roll()                # np.array of pinao roll in 16 channel in shape [channel, pitch, time]
# mid.save_npz("test.npz")
# mid.save_png("test.png")
# mid.save_mp3("test.mp3")
