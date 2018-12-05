# Day 1 - Use a Two Colour LED Module with micro:bit

https://www.littlebird.com.au/learn/62/use-a-two-colour-led-module-with-micro-bit

I'd had a play around with this module beforehand, just so I could hit the
ground running with the kids. I found I got better results using a 680R resistor
on the red pin, and a 100R on the green. This gave an even intensity between red
and green, and a clearly distinct yellow.

We started by just turning on the red led. Then played around setting the led to
green and orange.

Next up we turned the led on, and then off again. I got the kids to have a think
about why it didn't seem to work, and then we added a sleep in between.

We played around with a few different sleep times, then we extended that to make
a sequence of red, green, yellow.

The next step was to push that out into a while loop, to make it repeat the
sequence. This didn't work as expected, because we weren't turning off the green
pin at the start, and we had no sleep at the end. This led to a little more
thinking and debugging, and we ended up with our expected sequence.

The next step was to create a `sleep_time` variable, and change all the sleep
calls to use that. We then played around with different sleep times, and
experimented with how fast we could make it flash, while still being able to
see the different colours.

The final step was to create a `set_colour(red, green)` function, that sets the
pins and then sleeps. This may have been overkill, but I think this should lead
nicely into tomorrow's RGB led.
