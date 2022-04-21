from socket import *

port = int(input("Port No: "))
address = ('localhost', port)
BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Message to send: ")
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    print("Received message: %s" % data.decode())

s.close()
