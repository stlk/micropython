import time
from machine import Pin
from neopixel import NeoPixel
from fader import Fader

NEOPIXEL_COUNT = 8

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, NEOPIXEL_COUNT)

fader = Fader(np, NEOPIXEL_COUNT)

def set_color(color):
    np[0] = color
    for i in range(1, NEOPIXEL_COUNT):
        np[i] = (0, 0, 0)
    np.write()

def warn():
    set_color((255, 128, 0))

def error():
    set_color((255, 0, 0))

def beacon():
    fader.stop()
    for repeat in range(0, 10):
        for pos in range(0, NEOPIXEL_COUNT):
            for i in range(0, NEOPIXEL_COUNT):
                if i == pos:
                    np[i] = (249, 72, 119)
                else:
                    np[i] = (0, 0, 0)
            np.write()
            time.sleep_ms(100)
    fader.start()

def init():
    fader.start()

def violet():
    set_color((148, 0, 211))
