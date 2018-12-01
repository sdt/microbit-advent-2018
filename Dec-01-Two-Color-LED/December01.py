# December 1 2018
from microbit import *

sleep_time = 155

def set_colour(red, green):
    pin0.write_digital(red)
    pin1.write_digital(green)
    sleep(sleep_time)

while True:
    set_colour(1, 0)
    set_colour(1, 1)
    set_colour(0, 1)