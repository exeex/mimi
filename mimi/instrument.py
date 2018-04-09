class __Piano:
    def __init__(self):
        self.AcousticGrandPiano = 0
        self.BrightAcousticPiano = 1
        self.ElectricGrandPiano = 2
        self.Honky_tonkPiano = 3
        self.ElectricPiano1 = 4
        self.ElectricPiano2 = 5
        self.Harpsichord = 6
        self.Clavinet = 7


class __ChromaticPercussion:
    def __init__(self):
        self.Celesta = 8
        self.Glockenspiel = 9
        self.MusicBox = 10
        self.Vibraphone = 11
        self.Marimba = 12
        self.Xylophone = 13
        self.TubularBells = 14
        self.Dulcimer = 15


class __Organ:
    def __init__(self):
        self.DrawbarOrgan = 16
        self.PercussiveOrgan = 17
        self.RockOrgan = 18
        self.ChurchOrgan = 19
        self.ReedOrgan = 20
        self.Accordion = 21
        self.Harmonica = 22
        self.TangoAccordion = 23


class __Guitar:
    def __init__(self):
        self.AcousticGuitar_nylon = 24
        self.AcousticGuitar_steel = 25
        self.ElectricGuitar_jazz = 26
        self.ElectricGuitar_clean = 27
        self.ElectricGuitar_muted = 28
        self.OverdrivenGuitar = 29
        self.DistortionGuitar = 30
        self.GuitarHarmonics = 31


class __Bass:
    def __init__(self):
        self.AcousticBass = 32
        self.ElectricBass_finger = 33
        self.ElectricBass_pick = 34
        self.FretlessBass = 35
        self.SlapBass1 = 36
        self.SlapBass2 = 37
        self.SynthBass1 = 38
        self.SynthBass2 = 39


class __Strings:
    def __init__(self):
        self.Violin = 40
        self.Viola = 41
        self.Cello = 42
        self.Contrabass = 43
        self.TremoloStrings = 44
        self.PizzicatoStrings = 45
        self.OrchestralHarp = 46
        self.Timpani = 47


class __Ensemble:
    def __init__(self):
        self.StringEnsemble1 = 48
        self.StringEnsemble2 = 49
        self.SynthStrings1 = 50
        self.SynthStrings2 = 51
        self.ChoirAahs = 52
        self.VoiceOohs = 53
        self.SynthChoir = 54
        self.OrchestraHit = 55


class __Brass:
    def __init__(self):
        self.Trumpet = 56
        self.Trombone = 57
        self.Tuba = 58
        self.MutedTrumpet = 59
        self.FrenchHorn = 60
        self.BrassSection = 61
        self.SynthBrass1 = 62
        self.SynthBrass2 = 63


class __Reed:
    def __init__(self):
        self.SopranoSax = 64
        self.AltoSax = 65
        self.TenorSax = 66
        self.BaritoneSax = 67
        self.Oboe = 68
        self.EnglishHorn = 69
        self.Bassoon = 70
        self.Clarinet = 71


class __Pipe:
    def __init__(self):
        self.Piccolo = 72
        self.Flute = 73
        self.Recorder = 74
        self.PanFlute = 75
        self.Blownbottle = 76
        self.Shakuhachi = 77
        self.Whistle = 78
        self.Ocarina = 79


class __SynthLead:
    def __init__(self):
        self.Lead1_square = 80
        self.Lead2_sawtooth = 81
        self.Lead3_calliope = 82
        self.Lead4_chiff = 83
        self.Lead5_charang = 84
        self.Lead6_voice = 85
        self.Lead7_fifths = 86
        self.Lead8_bass_lead = 87


class __SynthPad:
    def __init__(self):
        self.Pad1_newage = 88
        self.Pad2_warm = 89
        self.Pad3_polysynth = 90
        self.Pad4_choir = 91
        self.Pad5_bowed = 92
        self.Pad6_metallic = 93
        self.Pad7_halo = 94
        self.Pad8_sweep = 95


class __SynthEffects:
    def __init__(self):
        self.FX1_rain = 96
        self.FX2_soundtrack = 97
        self.FX3_crystal = 98
        self.FX4_atmosphere = 99
        self.FX5_brightness = 100
        self.FX6_goblins = 101
        self.FX7_echoes = 102
        self.FX8_sci_fi = 103


class __Ethnic:
    def __init__(self):
        self.Sitar = 104
        self.Banjo = 105
        self.Shamisen = 106
        self.Koto = 107
        self.Kalimba = 108
        self.Bagpipe = 109
        self.Fiddle = 110
        self.Shanai = 111


class __Percussive:
    def __init__(self):
        self.TinkleBell = 112
        self.Agogo = 113
        self.SteelDrums = 114
        self.Woodblock = 115
        self.TaikoDrum = 116
        self.MelodicTom = 117
        self.SynthDrum = 118
        self.ReverseCymbal = 119


class __Soundeffects:
    def __init__(self):
        self.GuitarFretNoise = 120
        self.BreathNoise = 121
        self.Seashore = 122
        self.BirdTweet = 123
        self.TelephoneRing = 124
        self.Helicopter = 125
        self.Applause = 126
        self.Gunshot = 127


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