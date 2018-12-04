# December 4 2018
from microbit import pin1, pin2, sleep, button_a, button_b
from tm1637 import TM1637

stopwatch = TM1637(clk=pin1, dio=pin2)
running = True
time = 0

while True:
    if button_b.was_pressed():
        time = 0
    if button_a.was_pressed():
        if running:
            running = False
        else:
            running = True
    if running:
        time = time + 1
    stopwatch.number(time)