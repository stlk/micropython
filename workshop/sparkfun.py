import usocket as _socket

HOST = 'data.sparkfun.com'
PUBLIC_KEY = ''
PRIVATE_KEY = ''

def send_temperature(temperature):
    s = _socket.socket()
    addr = _socket.getaddrinfo(HOST, 80)[0][-1]
    s.connect(addr)

    data = b'temp=' + str(temperature)

    s.write('POST /input/' + PUBLIC_KEY + ' HTTP/1.0\r\n')
    s.write('Host: '+ HOST + '\r\n')
    s.write('Phant-Private-Key: ' + PRIVATE_KEY + '\r\n')
    s.write('Content-Type: application/x-www-form-urlencoded\r\n')
    s.write('Connection: close\r\n')
    s.write('Content-Length: ' + str(len(data)) + '\r\n\r\n')
    s.write(data)

    while True:
        data = s.recv(100)
        if data:
            chunk = str(data, 'utf8')
            print(chunk, end='')
        else:
            break

    s.close()

def read_temperature():
    pass # sem vloz kod pro cteni teploty
