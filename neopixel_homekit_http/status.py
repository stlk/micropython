from machine import Pin
from neopixel import NeoPixel

NEOPIXEL_COUNT = 8

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, NEOPIXEL_COUNT)

status = 0
color_hex = "ffffff"

def set_status(s):
    global status
    status = s
    update()

def set_color(c):
    global color_hex
    color_hex = c
    update()

def get_color():
    r, g, b = color_hex[:2], color_hex[2:4], color_hex[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r, g, b)

def update():
    if not status:
        write((0, 0, 0))
        return

    color = get_color()
    write(color)

def write(c):
    for i in range(0, NEOPIXEL_COUNT):
        np[i] = c
    np.write()
