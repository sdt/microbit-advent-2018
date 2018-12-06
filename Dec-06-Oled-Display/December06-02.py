# December 6
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()

add_text(0, 0, "STARS IN THE")
add_text(0, 1, "SKY THEY WAS")
add_text(0, 2, "TOLD BY A")
add_text(0, 3, "WARLOCK")