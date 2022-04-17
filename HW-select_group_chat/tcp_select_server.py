from socket import *
import select
import time

socks = []
BUFF = 1024
PORT = 9000

s_sock = socket()
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(str(PORT) + '에서 접속 대기 중')

while True:
    # socks의 길이가 1일 때 중지하기
    
    r_sock, w_sock, e_sock = select.select(socks, [], [])
    
    for s in r_sock:
        if s == s_sock:     # 클라이언트 accept 요청이 들어온 경우
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else:
            data = s.recv(BUFF).decode()
            if not data:
                s.close()
                socks.remove(s)
                continue
            if 'quit' in data:
                if s in socks:
                    s.close()
                    socks.remove(s)
                    continue

            print(time.asctime()+str(s)+':'+data)
            
            for ss in socks[1:]:
                print(ss)
                if ss != s:
                    ss.send(data.encode())