from socket import *
import threading

port = 9000
address = ('localhost', port)
BUFF = 1024

def handler(sock):
    while True:
        msg = sock.recv(BUFF)
        print(msg.decode())

s = socket(AF_INET, SOCK_STREAM)
s.connect(address)

id = input('ID를 입력하세요: ')
s.send(('['+id+']').encode())

th = threading.Thread(target=handler, args=(s,))
th.daemon = True
th.start()

while True:
    data = input()
    if data == 'q':
        s.send(data.encode())
        break

    full_data = '['+id+'] ' + data
    s.send(full_data.encode())

s.close()
