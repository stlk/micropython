from time import sleep
from status import np, NEOPIXEL_COUNT
from machine import Timer

def wheel(pos):
    pos = 255 - pos
    if pos < 85:
        return (255 - pos * 3, 0, pos * 3)
    if pos < 170:
        pos -= 85
        return (0, pos * 3, 255 - pos * 3)
    pos -= 170
    return (pos * 3, 255 - pos * 3, 0)

class Fader(object):
    def __init__(self):
        super(Fader, self).__init__()
        self.step = 0

    def rainbow_cycle(self):
        for i in range(0, NEOPIXEL_COUNT):
            np[i] = wheel(int(i * 256 / NEOPIXEL_COUNT + self.step) & 255)
        np.write()

    def tick(self, t):
        self.rainbow_cycle()
        self.step += 1
        if self.step > 256 * 5:
            self.step = 0

def init():
    fader = Fader()
    tim = Timer(-1)
    tim.init(period=40, mode=Timer.PERIODIC, callback=fader.tick)
