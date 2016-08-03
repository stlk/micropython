import time
from machine import Timer
from machine import Pin
import temperature
import mqtt

led = Pin(16, Pin.OUT)
tim = Timer(-1)

def tick(t):
    led.low()
    time.sleep_ms(200)
    led.high()

    temp = temperature.read_temp()
    mqtt.send(temp)

def start():
    tim.init(period=15000, mode=Timer.PERIODIC, callback=tick)

def stop():
    tim.deinit()
    print('timer stopped')
