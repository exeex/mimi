import mido
from mido import Message
from mimi.instrument import Piano
from mimi.Mimi import Note,Chord,Bar,Tab


class MidiTrack(mido.MidiTrack):

    def __init__(self,instrument= Piano.AcousticGrandPiano):
        super(MidiTrack,self).__init__()
        self.instrument = instrument
        self.append(Message('program_change', program=instrument, time=0))


    def append_bar(self, bar):
        if type(bar) is Bar:
            self.__append_bar(bar)

        elif type(bar) is Tab:
            for tab_bar in bar.bars:
                self.__append_bar(tab_bar)

    def __append_bar(self, bar: Bar):
        for note in bar.notes:

            if type(note) is Note:

                pitch = bar.to_128_pitch(note)
                time = bar.to_time(note)
                print(pitch, time, note)

                self.append(Message('note_on', note=pitch, velocity=64, time=0))
                self.append(Message('note_off', note=pitch, velocity=64, time=time))

            elif type(note) is Chord:

                pitch = 0
                time = bar.to_time(note)
                print(bar.to_128_pitch(note), time, note)

                for chord_note in note.chord:
                    pitch = bar.to_128_pitch(chord_note)
                    self.append(Message('note_on', note=pitch, velocity=64, time=0))

                self.append(Message('note_off', note=pitch, velocity=64, time=time))

                for chord_note in reversed(note.chord[:-1]):
                    pitch = bar.to_128_pitch(chord_note)
                    self.append(Message('note_off', note=pitch, velocity=64, time=0))

            # TODO: Volume control
            # TODO: time shift
            # TODO: independent end time for notes in chord
            # TODO: Program change ---> done, ready to be tested

        return


