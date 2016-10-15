from machine import Pin
from neopixel import NeoPixel

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 1)

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
    set_color((0, 0, 255))

def violet():
    set_color((148, 0, 211))
