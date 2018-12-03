# Day 4 - 4 Digit, 7 Segment Display Module

On day 3 I peeked at what was coming up for day 4. I saw there was a 7 segment display module with a driver chip on it. I'd seen no mention of this on the MicroPython site, so I decided I'd better have an early hunt around to see if this would be possible.

I found a [TM1637 module by Mike Causer on GitHub]([https://github.com/mcauser/microbit-tm1637), and with a bit of fiddling about, got it to work. Thanks Mike!

I used the Files mode of the Mu editor to copy the tm1637.py file to the Micro:Bit, then flashed some sample code. I kept getting out of memory errors. I found the trick was to not import everything from the microbit library, but only the things I needed.

eg. `from microbit import pin1, pin2, sleep`