import socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('localhost',9000)
    sock.connect(addr)
    
    msg = input()

    if msg == 'q':
        break

    sock.send(msg.encode())

    print(sock.recv(1024).decode())

    sock.close()