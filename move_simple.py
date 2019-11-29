from gpiozero import Motor
from time import sleep

motorRight = Motor(forward=10, backward=9)
motorLeft = Motor(forward=8, backward=7)


def stop():
    motorRight.stop()
    motorLeft.stop()


def forward(t):
    motorRight.forward()
    motorLeft.forward()
    sleep(t)


def backward(t):
    motorRight.backward()
    motorLeft.backward()
    sleep(t)


def left(t):
    motorRight.backward()
    motorLeft.forward()
    sleep(t)


def right(t):
    motorRight.forward()
    motorLeft.backward()
    sleep(t)
