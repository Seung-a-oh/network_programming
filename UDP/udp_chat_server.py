from socket import *

port = 3333
BUFF = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFF)
    print('<-', data.decode())
    resp = input('->')
    sock.sendto(resp.encode(), addr)