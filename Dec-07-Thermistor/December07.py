# December 2 2018
from microbit import *

while True:
    temp = pin1.read_analog()
    over = pin0.read_digital()
    if over == 1:
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)
    print((temp, over*500))
    sleep(100)