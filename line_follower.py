
import move
from gpiozero import LineSensor

# from gpiozero import LineSensor
# from signal import pause

# sensor = LineSensor(4)
# sensor.when_line = lambda: print('Line detected')
# sensor.when_no_line = lambda: print('No line detected')
# pause()

line_sensor = LineSensor(25)
speed = 0.5


# Search for the black line
def seek_line():
    print("Seeking the line")

    ret = False

    seek_size = 0.25  # Turn for 0.25s
    seek_count = 1  # A count of times the robot has looked for the line
    max_seek_count = 5  # The maximum time to seek the line in one direction
    direction = True  # The direction the robot will turn - True = Left

    while seek_count <= max_seek_count:
        # Set the seek time
        seek_time = seek_size * seek_count

        # Start the motors turning in a direction
        if direction:
            print("Looking left")
            move.left(speed)
        else:
            print("Looking Right")
            move.right(speed)

        line_sensor.wait_for_line(seek_time)
        if line_sensor.value() < 0.5:
            ret = True
        else:
            direction = not direction
            continue

    return ret


line_sensor.when_line = lambda: move.forward()
line_sensor.when_no_line = lambda: move.stop()

try:
    while True:
        move.forward(speed)
        line_sensor.wait_for_no_line()
        if not seek_line():
            print("Can't find any line")
            break

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    exit()
