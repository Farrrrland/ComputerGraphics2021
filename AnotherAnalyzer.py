#coding=utf-8
import numpy as np
import pyaudio
from pydub import AudioSegment, effects
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#------------------------------------两条线模式

AUDIO_DIR = "Music" + os.path.sep
CACHE_DIR = "Cache" + os.path.sep
IMAGE_DIR = "Image" + os.path.sep
AUDIO_NAME = "IceCream.wav"
IMAGE_NAME = "IceCream.gif"
root = os.getcwd()
AUDIO_DIR = root + os.path.sep + AUDIO_DIR
CACHE_DIR = root + os.path.sep + CACHE_DIR
IMAGE_DIR = root + os.path.sep + IMAGE_DIR

p = pyaudio.PyAudio()
sound = AudioSegment.from_file(AUDIO_DIR + AUDIO_NAME)
left = sound.split_to_mono()[0]
fs = left.frame_rate
size = len(left.get_array_of_samples())
channels = left.channels
stream = p.open(
    format=p.get_format_from_width(left.sample_width, ),
    channels=channels,
    rate=fs,
    # input=True,
    output=True,
)
stream.start_stream()

fig = plt.figure()
# ax1, ax2 = fig.subplots(2, 1)
ax1 = fig.subplots()
ax1.set_ylim(0, 2)
# ax2.set_ylim(-1.5, 1.5)
ax1.set_axis_off()
# ax2.set_axis_off()
window = int(0.02 * fs)  # 20ms

g_windows = window // 8


f = np.linspace(20, 20 * 1000, g_windows)
t = np.linspace(0, 20, window)
lf1, = ax1.plot(f, np.zeros(g_windows), lw=1)
lf1.set_antialiased(True)
# lf1.set_fillstyle('left')
# lf1.set_drawstyle('steps-pre')
# lf2, = ax2.plot(t, np.zeros(window), lw=1)

color_grade = ['black','blue','yellow','red']
def update(frames):
    if stream.is_active():
        slice = left.get_sample_slice(frames, frames + window)
        data = slice.raw_data
        stream.write(data)
        y = np.array(slice.get_array_of_samples()) / 30000  # 归一化
        yft = np.abs(np.fft.fft(y)) / (g_windows)
        # print('max',max(yft[:g_windows]),'min',min(yft[:g_windows]))
        # print(max(yft[:g_windows]) - min(yft[:g_windows]))
        # max =
        # min = min(yft[:g_windows])
        grade = int(max(yft[:g_windows]) - min(yft[:g_windows]))
        if 0 <= grade < len(color_grade):
            lf1.set_color(color_grade[grade])
        lf1.set_ydata(yft[:g_windows])
        # lf2.set_ydata(y)
    return lf1,
    # return lf1, lf2,


ani = FuncAnimation(fig, update, frames=range(0, size, window), interval=0, blit=True)
plt.savefig(IMAGE_DIR + IMAGE_NAME)
make_file_dir(IMAGE_DIR, IMAGE_NAME)
plt.show()