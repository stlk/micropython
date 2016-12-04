import socket
from machine import Pin
from neopixel import NeoPixel

NEOPIXEL_COUNT = 1

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, NEOPIXEL_COUNT)

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    color = ''
    while True:
        data = s.recv(100)
        if data:
            chunk = str(data, 'utf8')
            hash_index = chunk.find('#')
            if hash_index >= 0:
                color = chunk[hash_index + 1: hash_index + 7]
        else:
            break
    s.close()
    return color

def hex_color_to_tuple(color):
    red = (int(color, 16) >> 16) & 0xff
    green = (int(color, 16) >> 8) & 0xff
    blue = int(color, 16) & 0xff

    return (red, green, blue)

def set_color(color):
    np[0] = color
    np.write()

def update_color():
    color_hex = http_get('http://api.thingspeak.com/channels/1417/field/2/last.txt')
    print('received color', color_hex)
    color_tuple = hex_color_to_tuple(color_hex)
    print('converted color', color_tuple)
    set_color(color_tuple)
