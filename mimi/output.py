import os
from os.path import join, abspath, split
import platform

module_root_path = split(abspath(__file__))[0]
# set cfg_file to mimi/soundfont/8MBGMSFX.cfg
cfg_file = join(module_root_path, "soundfont","8MBGMSFX.cfg")

def set_soundfont(dir=None):

    # make cfg_file mimi/soundfont/8MBGMSFX.cfg point to soundfont file 8MBGMSFX.SF2

    if dir is None:
        with open(join(module_root_path,"soundfont","8MBGMSFX.cfg"),'w') as f:
            f.write("dir {} \nsoundfont \"8MBGMSFX.SF2\" amp=200%".format(join(module_root_path,"soundfont")))

    # TODO: user customized soundfont


def play(filename):
    # play by timidity
    _platform = platform.system()
    if _platform == "linux" or _platform == "linux2" or _platform == "Linux":
        os.system(
            "timidity -c %s %s -Ow -o - | ffmpeg -i - -map_channel 0.0.0 -f wav - | ffplay -i -" % (cfg_file, filename))
    else:
        os.system("timidity -c %s %s -A100" % (cfg_file,filename))




def midi2wav(mid_file = "gg.mid", outpath = "gg.wav"):
    # convert a mid file to wav file

    os.system("timidity -c %s %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f -A100 -Ow -o %s" %
                  (cfg_file, mid_file, outpath))

    # TODO: fix mp3 output
    # os.system("timidity -c .\8MBGMSFX.cfg %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f -A4 -Ow -o - | ffmpeg -i -  -vn -ar 44100 -ac 2 -ab 192k -f mp3 output.mp3" % filename)

def json(filename, json: str):

    # write json string to file

    with open(filename, "w") as f:
        f.write(json)

if __name__ == "__main__":
    play("test_file/1.mid")
    # print(join(split(abspath(__file__))[0],"soundfont"))
    # midi2wav("/Users/cswu/mimi/output/mid/gggg.mid")
    # json("./json/gg.json","{hello world}")
    # set_soundfont()