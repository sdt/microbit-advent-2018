# December 6
from ssd1306 import initialize, clear_oled
from ssd1306_stamp import draw_stamp
from ssd1306_img import create_stamp
from microbit import Image

initialize()
clear_oled()
stamp = create_stamp(Image.SNAKE)
y = 0
while True:
    for x in range(0, 58, +1):
        draw_stamp(x, y, stamp, 1, 1)
        draw_stamp(x, y, stamp, 0, 0)
    y = y + 1
    for x in range(57, 0, -1):
        draw_stamp(x, y, stamp, 1, 1)
        draw_stamp(x, y, stamp, 0, 0)
    y = y + 1