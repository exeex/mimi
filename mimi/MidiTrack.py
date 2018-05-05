import mido
from mido import Message
from mimi.instrument import Piano
from mimi.Mimi import Note, AbsNote, Chord, Bar, Tab
from typing import Union


class MidiTrack(mido.MidiTrack):

    def __init__(self, channel=0, instrument=Piano.AcousticGrandPiano):
        super(MidiTrack, self).__init__()
        self.__append = super(MidiTrack, self).append
        self.instrument = instrument
        self.channel = channel
        self.append(Message('program_change', program=instrument, time=0, channel=self.channel))

    def append(self, object: Union[AbsNote, Message, Bar, Tab]):
        """
        append music element to the track
        input type could be:

        * AbsNote : 一個音符，pitch以midi-128音階定義，時間長度為midi的時間長度
        * Message : midi messsage
        * Bar : 一個bar是一個小節
        * Tab : 一個tab是數個bar組成

        :param object: the music element to be appended
        :return:
        """
        if type(object) is Message:
            self.__append(object)

        elif type(object) is AbsNote:
            self.append(Message('note_on', note=object.pitch, velocity=64, time=0, channel=self.channel))
            self.append(Message('note_off', note=object.pitch, velocity=64, time=object.time, channel=self.channel))

        elif type(object) is Bar:
            self.__append_bar(object)

        elif type(object) is Tab:
            for bar in object.bars:
                self.__append_bar(bar)

    def __append_bar(self, bar: Bar):
        for note in bar.notes:

            if type(note) is Note:

                pitch = bar.to_128_pitch(note)
                time = bar.to_time(note)
                print(pitch, time, note)

                self.append(Message('note_on', note=pitch, velocity=64, time=0, channel=self.channel))
                self.append(Message('note_off', note=pitch, velocity=64, time=time, channel=self.channel))

            elif type(note) is Chord:

                pitch = 0
                time = bar.to_time(note)
                print("chord: ", time, note)

                for chord_note in note.chord:
                    pitch = bar.to_128_pitch(chord_note)
                    self.append(Message('note_on', note=pitch, velocity=64, time=0, channel=self.channel))

                self.append(Message('note_off', note=pitch, velocity=64, time=time, channel=self.channel))

                for chord_note in reversed(note.chord[:-1]):
                    pitch = bar.to_128_pitch(chord_note)
                    self.append(Message('note_off', note=pitch, velocity=64, time=0, channel=self.channel))

            # TODO: Volume control
            # TODO: time shift
            # TODO: independent end time for notes in chord
            # TODO: Program change ---> done, ready to be tested

        return
