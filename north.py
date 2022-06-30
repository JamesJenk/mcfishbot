#!/bin/python3

import pyscreenshot as ImageGrab
from subprocess import run
from time import sleep
from PIL import ImageOps
from pytesseract import image_to_string

sleep(1)

SET_WINDOW_CMD = 'xdotool windowactivate `xdotool search --name "Minecraft 1" | tail -1`' # Set a bash command for finding a window with the name 'Minecraft.1'
ESC_CMD = 'xdotool key Escape'
CODE_CMD = 'xdotool windowactivate `xdotool search --name "Visual Studio Code" | tail -1`' 
run(SET_WINDOW_CMD, shell=True)

sleep(0.5)

run(ESC_CMD, shell=True)

sleep(0.5)

image = ImageGrab.grab(bbox=(3, 355, 698, 382))

image = image.convert(mode='L')

sleep(0.75)

run(CODE_CMD, shell=True)


image = ImageOps.invert(image)

width = image.size[0] 
height = image.size[1] 

# Converts grey to white

for i in range(0,width):

    for j in range(0,height):
        data = image.getpixel((i,j))

        if data == 123:
            image.putpixel((i,j),(255))

image.save('north.png')
photo = open('north.png')
photo.show()
# text = image_to_string(photo)
# image.show()

# print(True)
# word_list = text.split()
# print(word_list[1])