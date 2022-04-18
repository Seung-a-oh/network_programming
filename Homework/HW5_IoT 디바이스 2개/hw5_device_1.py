from socket import *
import random

BUFF_SIZE = 1024
port = 5555

d1_sock = socket()
d1_sock.bind(('', port))
d1_sock.listen(2)

while True:
    c, addr = d1_sock.accept()

    data = c.recv(BUFF_SIZE).decode()
   
    temp = random.randint(0, 40)
    humid = random.randint(0, 100)
    lilum = random.randint(70, 150)

    if data == 'quit':
        break
    elif data == '1':
        res = "Temp="+str(temp)+", Humid="+str(humid)+", lilum="+str(lilum)+"\n\r"
        c.send(res.encode())