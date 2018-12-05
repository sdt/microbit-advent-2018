# December 5 2018
from microbit import *

while True:
    ppopp = pin0.read_analog()
    pin1.write_analog(ppopp)
    print((ppopp, ppopp/8, - ppopp, -ppopp/8))
    sleep(150)