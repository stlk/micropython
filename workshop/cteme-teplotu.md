# Čteme teplotu

Máme teplotní čidlo [DS18B20](https://www.sparkfun.com/products/245), které můžeme použít hodně jednoduše. Sensorů může být na jednom pinu více.

```python
import time
import machine
import onewire
import ds18x20

# the device is on GPIO12
dat = machine.Pin(5)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

# tell sensor to start reading temperature
ds.convert_temp()

# it takes up to 750ms to read the temperature
time.sleep_ms(750)

# we have just one sensor, so we want to read the first sensor
temp = ds.read_temp(roms[0])

print('temperature:', end=' ')
print(temp)
```
