from __future__ import print_function
import matplotlib.pyplot as plt
''' 
Preprocess audio
'''
import numpy as np
import librosa
import librosa.display
import os


import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)



def get_class_names(path="./mp3/"):  # class names are subdirectory names in Samples/ directory
    class_names = os.listdir(path)
    return class_names


def preprocess_dataset(inpath="./mp3/", outpath="./preproc/",fortest=False):
    if not os.path.exists(outpath):
        os.mkdir(outpath, mode=0o755);  # make a new directory for preproc'd files

    class_names = get_class_names(path=inpath)  # get the names of the subdirectories
    nb_classes = len(class_names)
    print("class_names = ", class_names)
    for idx, classname in enumerate(class_names):  # go through the subdirs

        if not os.path.exists(outpath + classname):
            os.mkdir(outpath + classname, 0o755);  # make a new subdirectory for preproc class

        if os.path.isdir(inpath + classname):
            class_files = os.listdir(inpath + classname)
        n_files = len(class_files)
        n_load = n_files
        print(' class name = {:14s} - {:3d}'.format(classname, idx),
              ", ", n_files, " files in this class", sep="")

        printevery = 20



        for idx2, infilename in enumerate(class_files):
            audio_path = inpath + classname + '/' + infilename

            # TODO : rewrite the dim of mel-spectrogram

            if (0 == idx2 % printevery):
                print('\r Loading class: {:14s} ({:2d} of {:2d} classes)'.format(classname, idx + 1, nb_classes),
                      ", file ", idx2 + 1, " of ", n_load, ": ", audio_path, sep="")
            # start = timer()
            try:
                aud, sr = librosa.load(audio_path, sr=None)
            except:
                eprint("load file {} failed".format(audio_path))
                raise
                pass

                mels = 256
                fft_window = 8192
                hop = 5645

                # frame_nb = sec * sr / hop


                melgram = librosa.logamplitude(librosa.feature.melspectrogram(aud, sr=sr, n_mels=mels, n_fft=fft_window, hop_length=hop), ref_power=1.0)[
                          np.newaxis, np.newaxis, :, :]
                outfile = outpath + classname + '/' + infilename + '.npy'

                if fortest:
                    print(melgram.shape)
                    print(sr)
                    print("%.1f" % (float(aud.shape[0])/float(sr)))
                    plt.figure()
                    librosa.display.specshow(melgram[0,0,:,:], y_axis='mel', hop_length=hop, sr=sr, fmax=sr//2, x_axis='time')
                    plt.colorbar(format='%+2.0f dB')
                    plt.show()
                    return

                np.save(outfile, melgram)



if __name__ == '__main__':
    preprocess_dataset(inpath = "./mp3/", fortest=True)
