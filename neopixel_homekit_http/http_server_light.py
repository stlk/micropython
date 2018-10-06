try:
    import usocket as socket
except:
    import socket

import status

CONTENT = b"""\
HTTP/1.0 200 OK

%s
"""

def get_command(response):
    response = response.decode("utf-8")
    start = response.find(" ")
    end = response.find(" ", start+1)

    return(response[start+1:end])

def main():
    s = socket.socket()
    ai = socket.getaddrinfo("0.0.0.0", 80)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening")

    while True:
        res = s.accept()
        client_sock = res[0]
        client_addr = res[1]
        print("Client address:", client_addr)
        print("Client socket:", client_sock)

        req = client_sock.recv(128)
        cmd = get_command(req)

        print("Request:")
        print(cmd)
        print()

        if (cmd == "/status"):
            client_sock.write(CONTENT % status.status)
        elif (cmd == "/on"):
            status.set_status(1)
            client_sock.write(CONTENT % status.status)
        elif (cmd == "/off"):
            status.set_status(0)
            client_sock.write(CONTENT % status.status)
        elif (cmd == "/c"):
            client_sock.write(CONTENT % status.color_hex)
        elif (cmd[:3] == "/c/"):
            status.set_color(cmd[3:])
            client_sock.write(CONTENT % "OK")
        else:
            client_sock.write(CONTENT % "OK")

        client_sock.close()
