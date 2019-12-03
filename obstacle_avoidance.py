#!/usr/bin/env python3

import move
import signal
from gpiozero import DistanceSensor

min_distance = 0.15
sonic_sensor = DistanceSensor(
    echo=18, trigger=17, threshold_distance=min_distance)
speed = 0.5


def exit_gracefully():
    exit()


sonic_sensor.when_in_range = lambda: move.stop()
sonic_sensor.when_out_of_range = lambda: move.forward()

signal.signal(signal.SIGINT, exit_gracefully)

move.forward(speed)
while True:
    sonic_sensor.wait_for_in_range()
    move.backward(speed)
    sonic_sensor.wait_for_out_of_range()
    move.right(speed, 0.75)


exit_gracefully()
