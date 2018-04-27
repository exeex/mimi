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
* 建議一個channel就配一個track
* 建議一個channel只配一種樂器，配兩種會有bug

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
mid.draw_roll()                         # 用matplot作圖
mid.play()                              # 用播放器放出聲音, windows和mac預設是用timidity, ubuntu是用ffplay
# roll = mid.get_roll()                 # np.array of pinao roll in 16 channel in shape [channel, pitch, time]
# mid.save_npz("test.npz")              # npz中有兩個array, instrument是標記每個channel用啥樂器, 另外一個是pinao roll(draw_roll畫出來的array)
# mid.save_png("test.png")              # piano roll的圖
# mid.save_mp3("test.mp3")              # 這個應該不用解釋
