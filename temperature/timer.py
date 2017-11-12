from machine import Timer
import temperature
import mqtt
import status

tim = Timer(-1)

def tick(t):
    mqtt.c.check_msg()
    temp = temperature.read_temp()
    mqtt.send(temp)

def start():
    tim.init(period=15000, mode=Timer.PERIODIC, callback=tick)

def stop():
    tim.deinit()
    print('timer stopped')
