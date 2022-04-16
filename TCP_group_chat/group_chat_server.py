from socket import *
import threading
import time
import sys

port = 9000
BUFF = 1024
clients = []

def echoTask(sock,addr):
    while True:
        data = sock.recv(BUFF).decode()

        if not data:
            break
        if 'q' in data:
            if sock in clients:
                print(sock, 'exited.')
                clients.remove(sock)
                print('종료')
                continue
        
        print(time.asctime()+str(addr)+':'+data)

        for client in clients:
            if client != sock:
                client.send(data.encode())
    sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',port))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print('connected by', addr)

    if conn not in clients:
        print('new client', conn)
        clients.append(conn)
        print(clients)

    th = threading.Thread(target=echoTask, args=(conn,addr))
    th.start()

