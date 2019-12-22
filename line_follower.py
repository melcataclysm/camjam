#!/usr/bin/env python3

import move
import signal
from gpiozero import LineSensor

line_sensor = LineSensor(25, pull_up=True)

speed = 0.4
move.speed_scale_left = 0.8
move.speed_scale_right = 1

def exit_gracefully(signal=None, stack=None):
    exit()


def seek_line():
    print("Seeking the line")

    ret = False

    seek_size = 0.35
    seek_count = 1
    max_seek_count = 5
    direction = False

    while seek_count <= max_seek_count:
        seek_time = seek_size * seek_count

        if direction:
            print("Looking left")
            move.left(speed)
        else:
            print("Looking right")
            move.right(speed)

        line_sensor.wait_for_line(seek_time)
        if line_sensor.value < 0.5:
            ret = True
            break
        else:
            direction = not direction
            if direction:
                seek_count += 1
            continue

    return ret


line_sensor.when_line = lambda: move.forward()
line_sensor.when_no_line = lambda: move.stop()

signal.signal(signal.SIGINT, exit_gracefully)

while True:
    move.forward(speed)
    line_sensor.wait_for_no_line()
    if not seek_line():
        print("Can't find any line")
        break

exit_gracefully()
