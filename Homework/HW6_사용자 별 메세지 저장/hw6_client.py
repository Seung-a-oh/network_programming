from socket import *

BUFF_SIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('Enter the message("send mboxId message" or "receive mboxId"):')
    c_sock.sendto(data.encode(),('localhost', port))

    if data == 'quit':
        break

    msg = c_sock.recv(BUFF_SIZE)
    print(msg.decode())
    
    if msg == 'Error':
        break
