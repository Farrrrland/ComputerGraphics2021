# Computer Graphics 2021
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Farrrrland/ComputerGraphics2021/HEAD)

Project of the Computer Graphics Course in Fudan University, Fall 2021

### Over View
The project is divided into 3 parts
1. Music visualization
2. Draw something with code
3. make a Flash vedio

This repo contains the first 2 of them. 
For Project 01, you are recommended to use Binder (repo2docker) to run the code, means you won't bother to deal with those environment setting stuffs, and there is no instrutions for you to set up on your own devices. Try it yourself if you'd like to.
For Project 02, you should run on your own device cuz there is no dependencies added for using turtle on Juypter Lab, If you want to do so, please modify the code on your own.

P.S. `./src/ ` folder is for ` README.md `, useless for the program

#### Part 1
Music Visualization

##### How to start
1. Click the ` lunch Binder ` Buttom and wait until the container is set
2. Pick Terminal in Jupyter Lab generated by Binder
3. Use the commend ` cd Project01_MusicVisualization/ ` to access project 01 dirctory
4. Use the commend ` python AudioAnalyzer.py ` to start processing music file and wait for the program to finish
5. Check the gif file you got in ` ./Image/ ` folder

You'll get ` .gif ` files like this:
![image](https://github.com/Farrrrland/ComputerGraphics2021/blob/main/readme.src/IceCream_README.gif)
You can also modify the Music files and try with your own ` .wav ` file. P.S. Only ` .wav ` file is valid here!

##### Main Code Logic
1. Use ` matplotlib ` in Python to draw the wave of a paticular interval of the music. (Here we use 1 Sec for a frame cuz this is the smallest interval for the data we got from ` AudioSegment.from_file `)
2. Save those waves as ` plt.plot ` and add to the frames list names ` ims [] `
3. Use ` animation.ArtistAnimation ` method to combine the frames and get the vedio
4. Save the vedio as ` .gif ` file

More details please refer to the code and I've written detailed comments for one to understand.

#### Part 2
Draw Something

##### How to start
1. Clone the code onto your device
2. Switch to the folder of PJ 2
3. Use the commend ` python DrawSomething.py ` to start drawing and wait for the program to finish (Turtle is needed for the code to run properly, so search the internet for this package)
4. You'll see PeppaPig as soon as it finishes

You'll get the tkinter window like this:

<img src="https://github.com/Farrrrland/ComputerGraphics2021/blob/main/readme.src/PeppaPig_Turtle.png" width = "60%" />
##### Main Code Logic
1. Use ` turtle ` in Python to draw the picture on canvas
3. See the documentations here about ` turtle `: https://docs.python.org/3/library/turtle.html
2. Follow the comments I made on the code, you can see the process of the drawing rather clearly
