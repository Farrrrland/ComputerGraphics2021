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
    # Load the music
    song = AudioSegment.from_mp3(file_path)
    # Get the splitted segment
    song = song[begin * SECOND: end * SECOND]
    # Save as cache
    cache_path = CACHE_DIR + file_path
    song.export(cache_path)
    return cache_path

if __name__ == '__main__':
    music, sr = librosa.load(split_music(0, 1, AUDIO_DIR + os.path.sep + AUDIO_NAME))
    # print a 14:5 Graph
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(music, sr=sr)
    plt.show()