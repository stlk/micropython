from machine import Pin
from neopixel import NeoPixel
from fader import Fader

NEOPIXEL_COUNT = 8

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, NEOPIXEL_COUNT)

fader = Fader(np, NEOPIXEL_COUNT)

def set_color(color):
    np[0] = color
    np.write()

def warn():
    set_color((255, 128, 0))

def error():
    set_color((255, 0, 0))

def ok():
    set_color((0, 255, 0))

def init():
    fader.start()

def violet():
    set_color((148, 0, 211))
