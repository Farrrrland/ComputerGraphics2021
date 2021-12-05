# Computer Graphics 2021
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Farrrrland/ComputerGraphics2021/HEAD)

Project of the Computer Graphics Course in Fudan University, Fall 2021

### Over View
The project is divided into 3 parts
1. Music visiualization
2. Draw something with code
3. make a Flash vedio
This repo contains the first 2 of them. You are recommended to use Binder (repo2docker) to run the code, means you won't bother to deal with those environment setting stuffs, and there is no instrutions for you to set up on your own devices. Try it yourself if you'd like to.

#### Part 1
Currently the repo contains only part one.

##### How to start
1. Click the ` lunch Binder ` Buttom and wait until the container is set
2. Pick Terminal in Jupyter Lab generated by Binder
3. Input the commend ` python AudioAnalyzer.py ` and wait for the program to finish
4. Check the gif file you got in ` ./Image/ ` folder
You can also modify the Music files and try with your own ` .wav ` file. P.S. Only ` .wav ` file is valid here!

##### Main Code Logic
1. Use ` matplotlib ` in Python to draw the wave of a paticular interval of the music. (Here we use 1 Sec for a frame cuz this is the smallest interval for the data we got from ` AudioSegment.from_file `)
2. Save those waves as ` plt.plot ` and add to the frames list names ` ims [] `
3. Use ` animation.ArtistAnimation ` method to combine the frames and get the vedio
4. Save the vedio as ` .gif ` file

More details please refer to the code and I've written detailed comments for one to understand.

