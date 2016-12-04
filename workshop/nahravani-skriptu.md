# Nahrávání skriptů

MicroPython hned po spuštění spustí skript `main.py`. To můžeme využít a nastavit náš modul, aby se vždy po spuštění připojil na wifi.

Vedle souboru `webrepl_cli.py` si vytvořme soubor `main.py` a vložme do něj kód, který jsme použili na připojení na wifi.

```python
SSID = 'TVOJE WIFI'
PASSWORD = 'TVOJE HESLO'
import network
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(SSID, PASSWORD)
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())
```

Pak ho tam nahrajme pomocí následujícího příkazu. Nejspíše budeš muset změnit IP adresu.

```
python webrepl_cli.py main.py 192.168.1.251:/
```

Výsledek by měl být následující
```
$ python webrepl_cli.py main.py 192.168.1.251:/
put 192.168.1.251 8266
main.py -> /main.py
Password:
Sent 311 of 311 bytes
```

Od teď pokaždé když modul spustíme v dosahu nastavené wifi, měl by se po startu připojit.
