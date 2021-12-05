import math
import os
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
from pydub import AudioSegment

SECOND = 1000
AUDIO_DIR = "Music" + os.path.sep
CACHE_DIR = "Cache" + os.path.sep
AUDIO_NAME = "IceCream.mp3"

def split_music (begin, end, file_path):
    print("[INFO]: file path is " + file_path)
    # Load the music
    song = AudioSegment.from_file(file_path)
    # print("[INFO]: End of AudioSegment")
    # Get the splitted segment
    song = song[begin * SECOND: end * SECOND]
    # Save as cache
    cache_path = CACHE_DIR + file_path
    song.export(cache_path)
    return cache_path

if __name__ == '__main__':
    root = os.getcwd()
    AUDIO_DIR = root + os.path.sep + AUDIO_DIR
    CACHE_DIR = root + os.path.sep + CACHE_DIR
    
    print("[INFO]: test dir " + AUDIO_DIR)
    music, sr = librosa.load(split_music(0, 1, AUDIO_DIR + AUDIO_NAME))
    # # music, sr = librosa.load(split_music(0, 15, AUDIO_NAME))
    # print a 14:5 Graph
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(music, sr=sr)
    plt.show()