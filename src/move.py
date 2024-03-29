from gpiozero import Motor
from time import sleep

motor_right = Motor(forward=10, backward=9)
motor_left = Motor(forward=8, backward=7)

speed_scale_right = 1
speed_scale_left = 1


def wait_and_stop(t):
    if t != 0:
        sleep(t)
        stop()


def stop():
    motor_right.stop()
    motor_left.stop()


def forward(s=1, t=0):
    motor_right.forward(s * speed_scale_right)
    motor_left.forward(s * speed_scale_left)
    wait_and_stop(t)


def backward(s=1, t=0):
    motor_right.backward(s * speed_scale_right)
    motor_left.backward(s * speed_scale_left)
    wait_and_stop(t)


def left(s=1, t=0):
    motor_right.backward(s * speed_scale_right)
    motor_left.forward(s * speed_scale_left)
    wait_and_stop(t)


def left_slow(s=1, t=0):
    motor_right.stop()
    motor_left.forward(s * speed_scale_left)
    wait_and_stop(t)


def right(s=1, t=0):
    motor_right.forward(s * speed_scale_right)
    motor_left.backward(s * speed_scale_left)
    wait_and_stop(t)


def right_slow(s=1, t=0):
    motor_right.forward(s * speed_scale_right)
    motor_left.stop()
    wait_and_stop(t)
