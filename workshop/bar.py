from machine import Pin
from neopixel import NeoPixel
import time
import temperature

NEOPIXEL_COUNT = 8

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, NEOPIXEL_COUNT)

RED = (16, 16, 0)
BLUE = (0, 0, 16)
OFF = (0, 0, 0)

def set_panel(temp):
    color = RED if temp > 0 else BLUE
    for i in range(NEOPIXEL_COUNT):
        np[i] = color if abs(temp) >= i + 1 else OFF
    np.write()

while True:
    temp = temperature.read_temp()
    set_panel(temp)
    time.sleep(1)
