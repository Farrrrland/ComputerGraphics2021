import math
import os
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
from pydub import AudioSegment

SECOND = 1000
AUDIO_DIR = "Music" + os.path.sep
CACHE_DIR = "Cache" + os.path.sep
IMAGE_DIR = "Image" + os.path.sep
AUDIO_NAME = "IceCream.wav"
IMAGE_NAME = "IceCream.jpg"

def make_file_dir(path, file_name):
    path_exist = os.path.exists(path)
    if not path_exist:
        os.makedirs(path)
    file = open(path + file_name, "w")
    file.close

def split_music(begin, end, audio_dir, cache_dir, audio_name):
    file_path = audio_dir + audio_name
    cache_path = cache_dir + audio_name
    print("[INFO]: file path is " + file_path)
    # Load the music
    song = AudioSegment.from_file(file_path)
    # print("[INFO]: End of AudioSegment")
    # Get the splitted segment
    song = song[begin * SECOND: end * SECOND]
    # Save as cache
    make_file_dir(cache_dir, audio_name)
    song.export(cache_path)
    return cache_path

if __name__ == '__main__':
    root = os.getcwd()
    AUDIO_DIR = root + os.path.sep + AUDIO_DIR
    CACHE_DIR = root + os.path.sep + CACHE_DIR
    IMAGE_DIR = root + os.path.sep + IMAGE_DIR
    
    print("[INFO]: test dir " + AUDIO_DIR)
    music, sr = librosa.load(split_music(0, 1, AUDIO_DIR, CACHE_DIR, AUDIO_NAME))
    # print a 14:5 Graph
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(music, sr=sr)
    plt.savefig(IMAGE_DIR + IMAGE_NAME)
    plt.show()