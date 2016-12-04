# Nastavení nahrávání skriptů, WebREPL

Připoj se k modulu

```
screen /dev/tty.wchusbserial1420 115200
```

Toto je příkaz na Macu, další platformy jsou popsány v sekci Instalace na http://pyladies.cz/v1/s016-micropython/index.html


```
��g�n�d��d�l��ld�Ä���l�n����cll�{pğ�#d�c{l{$s�'�����g����cpc�������bd���sb$`Ãl'�p;l�l��#4 ets_task(40100164, 3, 3fff8398, 4)
could not open file 'main.py' for reading

MicroPython v1.8.6-7-gefd0927 on 2016-11-10; ESP module with ESP8266
Type "help()" for more information.
>>>
```

Příkazem `import webrepl_setup` spustíme průvodce.

```
>>> import webrepl_setup
WebREPL daemon auto-start status: disabled

Would you like to (E)nable or (D)isable it running on boot?
(Empty line to quit)
> E
To enable WebREPL, you must set password for it
New password: heslicko
Confirm password: heslicko
Changes will be activated after reboot
Would you like to reboot now? (y/n)
> y
```

Po restatu si všimni `Started webrepl in normal mode`.

```
��g�n�d��d�l��ld��Č���l�o�����cdl�;x���#$�c;l{ls�n����cp�Č������bd���sb�b��o���b8cĜ�����cl���rcd`�d��|��{r'cǄl��c�c서ܜ<�d�bl$cl��do�d`��$g�8{$�$ܟ|���#5 ets_task(40100164, 3, 3fff8398, 4)
WebREPL daemon started on ws://192.168.4.1:8266
WebREPL daemon started on ws://0.0.0.0:8266
Started webrepl in normal mode
could not open file 'main.py' for reading

MicroPython v1.8.6-7-gefd0927 on 2016-11-10; ESP module with ESP8266
Type "help()" for more information.
>>>
```

Teď nastavíme wifi a připojíme se.
