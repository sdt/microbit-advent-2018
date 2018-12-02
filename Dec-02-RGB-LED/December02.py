# December 2 2018
from microbit import *

sleep_time = 500

def set_colour(red, green, blue):
    pin0.write_digital(red)
    pin1.write_digital(green)
    pin2.write_digital(blue)
    sleep(sleep_time)

while True:
    set_colour(0, 0, 1)
    set_colour(0, 1, 0)
    set_colour(1, 0, 0)
    set_colour(1, 0, 1)
    set_colour(1, 1, 1)
    set_colour(0, 1, 1)
    set_colour(1, 1, 0)