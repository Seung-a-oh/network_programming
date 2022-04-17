from socket import *
import threading

PORT = 9000
address = ('localhost', PORT)
BUFF = 1024

def handler(sock):
    while True:
        msg = sock.recv(BUFF)
        print(msg.decode())

id = input('ID를 입력하세요: ')

s = socket(AF_INET, SOCK_STREAM)
s.connect(address)

s.send(('['+id+']').encode())

th = threading.Thread(target=handler, args=(s,))
th.daemon = True
th.start()

while True:
    data = input()
    if data == 'quit':
        s.send(data.encode())
        break

    full_data = '['+id+'] ' + data
    s.send(full_data.encode())

s.close()
