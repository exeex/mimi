import platform
import os



import platform
import os


def play(filename):

    filename = os.path.join("/Users/cswu/wav2midi-cnn/scripts/mimi/",filename)

    if platform.system() == "Windows":
        os.system("timidity -c .\8MBGMSFX.cfg %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f" % filename)
    else:
        os.system("timidity  %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f" % filename)



def midi2mp3(mid_file= "gg.mid", output= "gg.wav"):

    outpath = u"/Users/cswu/wav2midi-cnn/scripts/mimi"
    output = os.path.join(outpath, output)

    if platform.system() == "Windows":
        os.system("timidity -c .\8MBGMSFX.cfg %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f -A100 -Ow -o %s" % (mid_file, output))
        # os.system("timidity -c .\8MBGMSFX.cfg %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f -A4 -Ow -o - | ffmpeg -i -  -vn -ar 44100 -ac 2 -ab 192k -f mp3 output.mp3" % filename)
    else:
        os.system("timidity -c ./8MBGMSFX.cfg %s  -Od --reverb=d --noise-shaping=4 -EwpvseToz -f -A100 -Ow -o %s" % (mid_file, output))

def json(filename, json: str):
    with open(filename,"w") as f:
        f.write(json)





if __name__ == "__main__":
    # play("ggg.mid")


    json("./json/gg.json","{hello world}")