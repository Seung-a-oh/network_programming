from socket import *
import random

BUFF_SIZE = 1024
port = 3333

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost',port))

f = 0
while True:
    data = input('-> ')
    
    if data == 'quit':
        c_sock.send('quit'.encode())
        break

    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + data
        c_sock.send(resp.encode())
        c_sock.settimeout(2)

        try:
            data = c_sock.recv(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
    
    if reTx == 4:
        c_sock.send(b'fail')
        print("fail")

    c_sock.settimeout(None)

    while True:
        data = c_sock.recv(BUFF_SIZE)
        data = data.decode()

        if data == 'quit':
            f = 1
            break
        elif data == 'fail':
            break
        
        if random.random() <= 0.5:
            continue
        else:
            c_sock.send(b'ack')
            print('<-', data)
            break
    
    if f == 1:
        break