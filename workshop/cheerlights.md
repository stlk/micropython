# Ovládáme světlo z internetu - CheerLights

Teď si vyzkoušíme, jak stáhnout informaci z internetu a podle ní nastavit barvu světelného pásu. Využijeme k tomu projekt CheerLights.

>  CheerLights is an “Internet of Things” project created by Hans Scharler that allows people’s lights all across the world to synchronize to one color set by Twitter. This is a way to connect physical things with social networking experiences.


Tuhle šílenou hromadu kódu jsem stáhl z [oficiální dokumentace](http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html#http-get-request) a jen trochu upravil. Je to hodně nízkoúrovňové stahování textu z internetu.

```python
import socket

url = 'http://api.thingspeak.com/channels/1417/field/2/last.txt'
_, _, host, path = url.split('/', 3)
ai = socket.getaddrinfo(host, 80)
print('Address infos:', ai)
addr = ai[0][-1]

print('Connect address:', addr)
s = socket.socket()
s.connect(addr)
s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
color = ''
while True:
    data = s.recv(100)
    if data:
        chunk = str(data, 'utf8')
        # print(chunk, end='')
        hash_index = chunk.find('#')
        if hash_index >= 0:
            color = chunk[hash_index + 1: hash_index + 7]
    else:
        break
s.close()
print(color)
```

Vidíme, že jako odpověď dostaneme barvu, kterou máme zobrazit v HEX formátu. Po chvíli googlování jsem našel způsob jak tuto hodnotu převést na tuple barev `(255, 255, 255)`.

```python
color = 'ff9900'

red = (int(color, 16) >> 16) & 0xff
green = (int(color, 16) >> 8) & 0xff
blue = int(color, 16) & 0xff

print('red', red, 'green', green, 'blue', blue)
```
