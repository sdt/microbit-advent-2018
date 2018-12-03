# December 3 2018
from microbit import *

while True:
    bigbamboo = pin0.read_digital()
    if bigbamboo == 0:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)