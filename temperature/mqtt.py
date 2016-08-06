from simple import MQTTClient
from settings import MQTT_HOSTNAME

c = MQTTClient('umqtt_client', MQTT_HOSTNAME)
c.connect()
c.publish(b'status', b'hi')


def send(temp):
    c.publish(b'temp', b'%s' % (temp,))
