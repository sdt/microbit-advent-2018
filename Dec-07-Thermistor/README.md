# Day 7 - Thermistor

This one was a bit of a dud. Ah well, they can't all be gems.

We used the Mu plotter again, but we didn't manage to get the thermistor to do anything interesting. Holding it with our fingers tended to make the value drop a tiny bit, but most of that seemed to be noise introduced by wiggling the pins in the breadboard. Putting an ice pack on the thermistor didn't seem to make any difference at all.

I was curious about the digital pin. The IC on the board is an LM393 which is a comparator. I suspected the trimpot might be to set a threshold voltage, which would trigger the digital pin. We set up an led to reflect the digital pin, and adjusted the trimpot. The led started on, and we made it go out. We played with the trimpot some more, but it didn't come back on. Some kind of single shot perhaps.
