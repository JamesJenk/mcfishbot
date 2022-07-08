#!/bin/bash

xdotool windowactivate `xdotool search --name "Minecraft 1" | tail -1`
sleep 1
xdotool key Escape
sleep 1

while true

do

    xdotool click 1

    sleep 3

done