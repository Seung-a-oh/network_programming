from socket import *
import random

BUFF_SIZE = 1024
port = 6666

d2_sock = socket()
d2_sock.bind(('', port))
d2_sock.listen(2)

while True:
    c, addr = d2_sock.accept()

    data = c.recv(BUFF_SIZE).decode()

    heratbeat = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)

    if data == 'quit':
        break
    elif data == '2':
        res = "Hearthbeat="+str(heratbeat)+", Steps="+str(steps)+", Cal="+str(cal)+"\n\r"
        c.send(res.encode())

    