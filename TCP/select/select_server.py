import socket, select

socks = []
BUFF = 1024
PORT = 9000

s_sock = socket.socket()
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(str(PORT) + '에서 접속 대기 중')

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])
    print(r_sock)
    
    for s in r_sock:
        print("s:",s)
        if s == s_sock:
            print("first")
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
            print("second")
        else:
            print("third")
            data = s.recv(BUFF)
            print("fourth")
            if not data:
                s.close()
                socks.remove(s)
                continue
            print('Received:', data.decode())
            s.send(data)