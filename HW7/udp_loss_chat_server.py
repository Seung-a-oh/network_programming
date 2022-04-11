from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

f = 0
while True:
    sock.settimeout(None)
    
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        data = data.decode()
        if data == 'quit':
            f = 1
            break
        elif data == 'fail':
            break
        
        if random.random() <= 0.5:
            # ACK를 전달하지 않음
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data)
            break

    if f == 1:
        break

    msg = input('-> ')

    if msg == 'quit':
        sock.sendto('quit'.encode(), addr)
        break

    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    if reTx == 4:
        sock.sendto(b'fail', addr)
        print("fail")
