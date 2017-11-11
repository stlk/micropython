from machine import Timer

def brightness(colors, brightness = 0.2):
    r, g, b = colors
    return (int(r * brightness), int(g * brightness), int(b * brightness))

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
    def __init__(self, np, NEOPIXEL_COUNT):
        super(Fader, self).__init__()
        self.step = 0
        self.np = np
        self.NEOPIXEL_COUNT = NEOPIXEL_COUNT
        self.tim = Timer(-1)

    def start(self):
        self.tim.init(period=40, mode=Timer.PERIODIC, callback=self.tick)

    def stop(self):
        self.tim.deinit()

    def rainbow_cycle(self):
        for i in range(0, self.NEOPIXEL_COUNT):
            self.np[i] = brightness(wheel(int(i * 256 / self.NEOPIXEL_COUNT + self.step) & 255))
        self.np.write()

    def tick(self, t):
        self.rainbow_cycle()
        self.step += 1
        if self.step > 256 * 5:
            self.step = 0
