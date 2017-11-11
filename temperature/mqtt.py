import network
from simple import MQTTClient
from settings import MQTT_HOSTNAME, MQTT_PORT, MQTT_USER, MQTT_PASSWORD
import status

c = MQTTClient('umqtt_client',
               MQTT_HOSTNAME,
               port = MQTT_PORT,
               user = MQTT_USER,
               password = MQTT_PASSWORD)

try:
    c.connect()
    c.publish(b'status', b'hi')
except:
    status.error()
    print('MQTT hello failed')

try:
    sta_if = network.WLAN(network.STA_IF)
    c.publish(b'status', b'ip: %s' % (sta_if.ifconfig()[0],))
except:
    print('MQTT IP publish failed')

def publish(temp):
    c.publish(b'temp', b'%s' % (temp,))
    status.ok()

def send(temp):
    try:
        publish(temp)
    except:
        status.error()
        print('MQTT publish failed')
