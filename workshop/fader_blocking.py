from time import sleep
from machine import Pin
from neopixel import NeoPixel

NEOPIXEL_COUNT = 8

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, NEOPIXEL_COUNT)

def wheel(pos):
    pos = 255 - pos
    if pos < 85:
        return (255 - pos * 3, 0, pos * 3)
    if pos < 170:
        pos -= 85
        return (0, pos * 3, 255 - pos * 3)
    pos -= 170
    return (pos * 3, 255 - pos * 3, 0)

def rainbow_cycle():
    for step in range(0, 256 * 5):
        for i in range(0, NEOPIXEL_COUNT):
            np[i] = wheel(int(i * 256 / NEOPIXEL_COUNT + step) & 255)
        np.write()
        time.sleep_ms(1)

while True:
    rainbow_cycle()
