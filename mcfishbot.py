#!/bin/python

# System requirements: A software that can interpret bash, xdotool needs to be installed (it's free)

# Importing modules for the bot to work
from time import sleep
import numpy as np
from pyautogui import press, rightClick, position, size, screenshot
from PIL import ImageGrab
from subprocess import run, Popen, PIPE

SET_WINDOW_CMD = 'xdotool windowactivate `xdotool search --name "Minecraft 1.*"`' # Set a bash command for finding a window with the name 'Minecraft.1'
GET_WINDOW_GEOMETRY = 'xdotool getwindowgeometry `xdotool search --name "Minecraft 1.*"`' # Set a bash command for finding the size (in pixels)
RIGHT_CLICK = 'xdotool click 3' # Set a bash command for right clicking in bash

run(SET_WINDOW_CMD, shell=True) # This runs the command in your 

# Leave time for the window to activate
sleep(0.5)
press('esc') # This key is pressed to bring your computer out of the pause game screen

geometry = run(GET_WINDOW_GEOMETRY, shell=True, text=True, stdout=PIPE).stdout.split() # running the command in bash, ouptut is assigned to list
# splitting the output in a string (the element) into a list for easier access to information
pos_text = geometry[3].split(',')
size_text = geometry[7].split('x')
# The window position on the screen
pos_x = int(pos_text[0]) 
pos_y = int(pos_text[1])

# The window dimensions
size_x = int(size_text[0])
size_y = int(size_text[1])
x, y = position()
side_size = int(size_x / 32) if size_x >= 128 else 4
# print(pos_x, pos_y, size_x, size_y)


# Need some time for the menu GUIO to clear before taking the first screen shot
sleep(0.5)

# Get screenshot
average = 150.0 # set an estimated average
count = 100 # set an estimated count
for i in range(1000):
    image = ImageGrab.grab(bbox=(x-side_size, y-side_size, x+side_size, y+side_size)) # Takes an image box based off the centre of the screen
    image = image.convert('L') # Convert image into greyscale
    data = np.histogram(np.array(image), bins=16, range=(0,16)) # Converts the image into a histogram
    threshold = average / 3 # The threshold is a third of the average black found on the image
    average = (average * count + data[0][0]) / (count + 1) # This calculates the average
    count += 1
    if data[0][0] < threshold: 
        run(RIGHT_CLICK, shell=True) # This right clicks with xdotool in bash, pulls fishing rod back
        sleep(2)  # wait a couple of seconds before taking captures
        run(RIGHT_CLICK, shell=True) # Throw's rod back in
        sleep(1)
    print('Data: ', data[0][0], 'Threshold: ', threshold)
    sleep(0.1)

image.show() # Shows the image taken