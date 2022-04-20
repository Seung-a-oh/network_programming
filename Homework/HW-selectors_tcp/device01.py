from socket import *
import random
import time
import threading

BUFF_SIZE = 1024
port = 5555
BUFF = 1024

d1_sock = socket()
d1_sock.connect(('localhost',port))

# def quit(sock):
#     while True:
#         msg = input()
#         sock.send(msg)

# th = threading.Thread(target=quit, args=(d1_sock,))
# th.daemon = True
# th.start()

msg = d1_sock.recv(BUFF_SIZE)
if msg == b'register':
    while True:
        try:
            temp = random.randint(0, 40)
            humid = random.randint(0, 100)
            lilum = random.randint(70, 150)

            res = "1Temp="+str(temp)+", Humid="+str(humid)+", lilum="+str(lilum)+"\n"
            d1_sock.send(res.encode())
            time.sleep(3)
        except:
            d1_sock.send(b'quit')
