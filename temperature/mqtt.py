from simple import MQTTClient

c = MQTTClient('umqtt_client', 'HOSTNAME')
c.connect()
c.publish(b'status', b'hi')


def send(temp):
    c.publish(b'temp', b'%s' % (temp,))
