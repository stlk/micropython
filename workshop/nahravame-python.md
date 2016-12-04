# Nahráváme python
# Tato sekce je nutná, pouze pokud chceš aktualizovat MicroPython

http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html

Na pythonu 2 nainstalovat `esptool`

```
pip install esptool
```

Smazat program
```
esptool.py --port /dev/ttyUSB0 erase_flash
```
nebo
```
esptool.py --port /dev/tty.wchusbserial1420 erase_flash
```

Mělo by to vypadat takto:
```
$ esptool.py --port /dev/tty.wchusbserial1420 erase_flash
esptool.py v1.2.1
Connecting...
Running Cesanta flasher stub...
Erasing flash (this may take a while)...
Erase took 12.3 seconds
```

Stáhnout firmware z
http://www.micropython.org/download#esp8266

Nahrát nový
```
esptool.py --port /dev/ttyUSB0 write_flash --flash_size=detect 0 esp8266-20161110-v1.8.6.bin
```
nebo
```
esptool.py --port /dev/tty.wchusbserial1420 write_flash --flash_size=detect 0 esp8266-20161110-v1.8.6.bin
```

Mělo by to vypadat takto:
```
$ esptool.py --port /dev/tty.wchusbserial1420 write_flash --flash_size=detect 0 esp8266-20161110-v1.8.6.bin
esptool.py v1.2.1
Connecting...
Auto-detected Flash size: 32m
Running Cesanta flasher stub...
Flash params set to 0x0040
Writing 569344 @ 0x0... 569344 (100 %)
Wrote 569344 bytes at 0x0 in 49.4 seconds (92.2 kbit/s)...
Leaving...
```
