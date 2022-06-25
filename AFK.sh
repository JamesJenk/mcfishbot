#!/bin/bash

while true

do

    sleep 3

    xdotool key --delay 500 w

    echo "W key executed for 500 miliseconds."

    sleep 1

    xdotool key --delay 500 s

    echo "S key executed for 500 miliseconds."

    sleep 1

    xdotool click 1

    sleep 1

    # For timeout and reset

    d=$(date +"%M")

    if [ $d = '20' ]

    then

        echo "Timeout and reset check executed"
        
        xdotool mousemove 803 513 click 1 

        sleep 1

        xdotool key Tab

        sleep 1

        xdotool key Return

        sleep 1

    elif [ $d = '40' ]

    then

        echo "Timeout and reset check executed"

        xdotool mousemove 803 513 click 1 

        sleep 1

        xdotool key Tab

        sleep 1

        xdotool key Return

        sleep 1
    
    elif [ $d = '20' ]

    then
        
        echo "Timeout and reset check executed"

        xdotool key Tab

        sleep 1

        xdotool key Return

        sleep 1

        xdotool key Tab

        sleep 1

        xdotool key Return

        sleep 1

    else

    echo "Not time yet"; echo $d

    fi


done