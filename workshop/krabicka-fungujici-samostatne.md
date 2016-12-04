# Krabička fungující samostatně

Na konec souboru `main.py`, který jsme vytvořili kvůli Wi-Fi. Přidej následující kód.

```python
import sparkfun
import cheerlights
import time

while True:
    cheerlights.update_color()
    temp = sparkfun.read_temperature()
    sparkfun.send_temperature(temp)
    time.sleep(30)
```
