# Homebridge RGB light

A client device managed by https://github.com/jnovack/homebridge-better-http-rgb

### Homebridge config

```
{
    "bridge": {
        "name": "Homebridge",
        "username": "CC:22:3D:E3:CE:30",
        "port": 51826,
        "pin": "031-45-154"
    },
    "description": "",
    "accessories": [
        {
            "accessory": "HTTP-RGB",
            "name": "Light Box",
            "service": "Light",
            "switch": {
                "status": "http://192.168.1.80/status",
                "powerOn": "http://192.168.1.80/on",
                "powerOff": "http://192.168.1.80/off"
            },
            "color": {
                "status": "http://192.168.1.80/c",
                "url": "http://192.168.1.80/c/%s",
                "brightness": true
            }
        }
    ],
    "platforms": []
}
```