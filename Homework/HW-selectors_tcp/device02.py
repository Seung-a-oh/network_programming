from socket import *
import random
import time

BUFF_SIZE = 1024
port = 5555
BUFF = 1024

d2_sock = socket()
d2_sock.connect(('localhost',port))

msg = d2_sock.recv(BUFF_SIZE)
if msg == b'register':
    while True:   
        try:
            heratbeat = random.randint(40, 140)
            steps = random.randint(2000, 6000)
            cal = random.randint(1000, 4000)

            res = "2Heartbeat="+str(heratbeat)+", Steps="+str(steps)+", Cal="+str(cal)+"\n"
            d2_sock.send(res.encode())
            time.sleep(3)
        except:
            d2_sock.send(b'quit')

# 문제점: 키보드 익셉션이 발생했을 때 정보가 전달 될 수 있다.