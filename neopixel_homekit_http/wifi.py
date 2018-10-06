from settings import SSID, PASSWORD, IF_CONFIG

def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)

    if IF_CONFIG:
        sta_if.ifconfig(IF_CONFIG)

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
