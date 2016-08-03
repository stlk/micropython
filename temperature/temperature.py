import time
import machine
import onewire


def read_temp():
    # the device is on GPIO12
    dat = machine.Pin(5)

    # create the onewire object
    ds = onewire.DS18B20(onewire.OneWire(dat))

    # scan for devices on the bus
    roms = ds.scan()
    print('found devices:', roms)
    print('temperature:', end=' ')
    ds.convert_temp()
    time.sleep_ms(750)
    temp = ds.read_temp(roms[0])
    print(temp)
    return temp
