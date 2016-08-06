from simple import MQTTClient
from settings import MQTT_HOSTNAME

c = MQTTClient('umqtt_client', MQTT_HOSTNAME)

try:
    c.connect()
    c.publish(b'status', b'hi')
except:
    print('MQTT hello failed')


def publish(temp):
    c.publish(b'temp', b'%s' % (temp,))

def send(temp):
    try:
        publish(temp)
    except:
        print('MQTT retry')
        c.connect()
        publish(temp)
