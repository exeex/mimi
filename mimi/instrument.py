class __Piano:
    def __init__(self):
        self.AcousticGrandPiano = 1
        self.BrightAcousticPiano = 2
        self.ElectricGrandPiano = 3
        self.Honky_tonkPiano = 4
        self.ElectricPiano1 = 5
        self.ElectricPiano2 = 6
        self.Harpsichord = 7
        self.Clavinet = 8


class __ChromaticPercussion:
    def __init__(self):
        self.Celesta = 9
        self.Glockenspiel = 10
        self.MusicBox = 11
        self.Vibraphone = 12
        self.Marimba = 13
        self.Xylophone = 14
        self.TubularBells = 15
        self.Dulcimer = 16


class __Organ:
    def __init__(self):
        self.DrawbarOrgan = 17
        self.PercussiveOrgan = 18
        self.RockOrgan = 19
        self.ChurchOrgan = 20
        self.ReedOrgan = 21
        self.Accordion = 22
        self.Harmonica = 23
        self.TangoAccordion = 24


class __Guitar:
    def __init__(self):
        self.AcousticGuitar_nylon = 25
        self.AcousticGuitar_steel = 26
        self.ElectricGuitar_jazz = 27
        self.ElectricGuitar_clean = 28
        self.ElectricGuitar_muted = 29
        self.OverdrivenGuitar = 30
        self.DistortionGuitar = 31
        self.GuitarHarmonics = 32


class __Bass:
    def __init__(self):
        self.AcousticBass = 33
        self.ElectricBass_finger = 34
        self.ElectricBass_pick = 35
        self.FretlessBass = 36
        self.SlapBass1 = 37
        self.SlapBass2 = 38
        self.SynthBass1 = 39
        self.SynthBass2 = 40


class __Strings:
    def __init__(self):
        self.Violin = 41
        self.Viola = 42
        self.Cello = 43
        self.Contrabass = 44
        self.TremoloStrings = 45
        self.PizzicatoStrings = 46
        self.OrchestralHarp = 47
        self.Timpani = 48


class __Ensemble:
    def __init__(self):
        self.StringEnsemble1 = 49
        self.StringEnsemble2 = 50
        self.SynthStrings1 = 51
        self.SynthStrings2 = 52
        self.ChoirAahs = 53
        self.VoiceOohs = 54
        self.SynthChoir = 55
        self.OrchestraHit = 56


class __Brass:
    def __init__(self):
        self.Trumpet = 57
        self.Trombone = 58
        self.Tuba = 59
        self.MutedTrumpet = 60
        self.FrenchHorn = 61
        self.BrassSection = 62
        self.SynthBrass1 = 63
        self.SynthBrass2 = 64


class __Reed:
    def __init__(self):
        self.SopranoSax = 65
        self.AltoSax = 66
        self.TenorSax = 67
        self.BaritoneSax = 68
        self.Oboe = 69
        self.EnglishHorn = 70
        self.Bassoon = 71
        self.Clarinet = 72


class __Pipe:
    def __init__(self):
        self.Piccolo = 73
        self.Flute = 74
        self.Recorder = 75
        self.PanFlute = 76
        self.Blownbottle = 77
        self.Shakuhachi = 78
        self.Whistle = 79
        self.Ocarina = 80


class __SynthLead:
    def __init__(self):
        self.Lead1_square = 81
        self.Lead2_sawtooth = 82
        self.Lead3_calliope = 83
        self.Lead4_chiff = 84
        self.Lead5_charang = 85
        self.Lead6_voice = 86
        self.Lead7_fifths = 87
        self.Lead8_bass_lead = 88


class __SynthPad:
    def __init__(self):
        self.Pad1_newage = 89
        self.Pad2_warm = 90
        self.Pad3_polysynth = 91
        self.Pad4_choir = 92
        self.Pad5_bowed = 93
        self.Pad6_metallic = 94
        self.Pad7_halo = 95
        self.Pad8_sweep = 96


class __SynthEffects:
    def __init__(self):
        self.FX1_rain = 97
        self.FX2_soundtrack = 98
        self.FX3_crystal = 99
        self.FX4_atmosphere = 100
        self.FX5_brightness = 101
        self.FX6_goblins = 102
        self.FX7_echoes = 103
        self.FX8_sci_fi = 104


class __Ethnic:
    def __init__(self):
        self.Sitar = 105
        self.Banjo = 106
        self.Shamisen = 107
        self.Koto = 108
        self.Kalimba = 109
        self.Bagpipe = 110
        self.Fiddle = 111
        self.Shanai = 112


class __Percussive:
    def __init__(self):
        self.TinkleBell = 113
        self.Agogo = 114
        self.SteelDrums = 115
        self.Woodblock = 116
        self.TaikoDrum = 117
        self.MelodicTom = 118
        self.SynthDrum = 119
        self.ReverseCymbal = 120


class __Soundeffects:
    def __init__(self):
        self.GuitarFretNoise = 121
        self.BreathNoise = 122
        self.Seashore = 123
        self.BirdTweet = 124
        self.TelephoneRing = 125
        self.Helicopter = 126
        self.Applause = 127
        self.Gunshot = 128


Piano = __Piano()
ChromaticPercussion = __ChromaticPercussion()
Organ = __Organ()
Guitar = __Guitar()
Bass = __Bass()
Strings =__Strings()
Ensemble =__Ensemble()
Brass = __Brass()
Reed = __Reed()
Pipe = __Pipe()
SynthLead = __SynthLead()
SynthPad = __SynthPad()
SynthEffect = __SynthEffects()
Ethnic = __Ethnic()
Percussive = __Percussive()