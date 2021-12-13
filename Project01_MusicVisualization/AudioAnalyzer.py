import math
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import librosa.display
import numpy as np
from pydub import AudioSegment

# Modified by Farland

# Some Macros
SECOND = 1000
INTERVAL = 200
AUDIO_DIR = "Music" + os.path.sep
CACHE_DIR = "Cache" + os.path.sep
IMAGE_DIR = "Image" + os.path.sep
AUDIO_NAME = "IceCream.wav"
FILM_NAME = "IceCream.gif"

def make_file_dir(path, file_name):
    path_exist = os.path.exists(path)
    if not path_exist:
        os.makedirs(path)
    file = open(path + file_name, "w")
    file.close

def split_music(begin, end, song, cache_dir, audio_name):
    cache_path = cache_dir + audio_name
    # Get the splitted segment
    song = song[begin: end]
    # Save as cache, rewrite each time so not many extra memories required
    make_file_dir(cache_dir, audio_name)
    song.export(cache_path)
    return cache_path

if __name__ == '__main__':

    # Get current root so can run correctly in Binder
    root = os.getcwd()
    AUDIO_DIR = root + os.path.sep + AUDIO_DIR
    CACHE_DIR = root + os.path.sep + CACHE_DIR
    IMAGE_DIR = root + os.path.sep + IMAGE_DIR
    
    # Frames
    ims = []
    # Print a 14:5 Graph
    fig = plt.figure(figsize=(14, 5))
    # Load the music
    song = AudioSegment.from_file(AUDIO_DIR + AUDIO_NAME)
    for i in range(0, 120 * SECOND, SECOND):
        music, sr = librosa.load(split_music(i, i + SECOND, song, CACHE_DIR, AUDIO_NAME))
        n0 = 9000
        n1 = 10000
        # Get the upper part of the wave and do the zooming
        music = np.array([mic for mic in music if mic > 0])
        ims.append(plt.plot(music[n0:n1]))
        if i % (10 * SECOND) is 0:
            print("[INFO]: Processing... " + str(i / SECOND) + "s")
    # Generate gif file and save in ./Image/ folder
    ani = animation.ArtistAnimation(fig = fig, artists = ims, repeat = False, interval = 200)
    make_file_dir(IMAGE_DIR, FILM_NAME)
    ani.save(IMAGE_DIR + FILM_NAME, fps=5)