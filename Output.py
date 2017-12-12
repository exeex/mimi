import platform
import os
from os.path import join, abspath, split


def play(filename):

    filename = os.path.join("/Users/cswu/wav2midi-cnn/scripts/mimi/", filename)

    if platform.system() == "Windows":
        os.system("timidity -c .\8MBGMSFX.cfg %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f" % filename)
    else:
        os.system("timidity  %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f" % filename)


def midi2wav(mid_file = "gg.mid", outpath = "gg.wav"):

    module_root_path = split(abspath(__file__))[0]
    cfg_file = join(module_root_path, "soundfont","8MBGMSFX.cfg")
    os.system("timidity -c %s %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f -A100 -Ow -o %s" %
                  (cfg_file, mid_file, outpath))

    # os.system("timidity -c .\8MBGMSFX.cfg %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f -A4 -Ow -o - | ffmpeg -i -  -vn -ar 44100 -ac 2 -ab 192k -f mp3 output.mp3" % filename)

def json(filename, json: str):
    with open(filename, "w") as f:
        f.write(json)

if __name__ == "__main__":
    # play("ggg.mid")
    # print(join(split(abspath(__file__))[0],"soundfont"))
    midi2wav("/Users/cswu/mimi/output/mid/gggg.mid")
    # json("./json/gg.json","{hello world}")