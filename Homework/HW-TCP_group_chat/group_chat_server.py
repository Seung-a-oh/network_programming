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
        if 'quit' in data:
            if sock in clients:
                print('현재 스레드 개수:',threading.active_count())
                print('현재 클라이언트 수:',clients)
                print(addr, 'exited.')
                clients.remove(sock)
                print('종료')
                sock.close()
                print('종료 후 클라이언트 수:',clients)
                print('종료 후 스레드 개수:',threading.active_count())
                break
        
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

