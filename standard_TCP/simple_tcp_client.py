from socket import *

sock = socket(AF_INET, SOCK_STREAM)
addr = ('localhost',2500)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())
sock.close()