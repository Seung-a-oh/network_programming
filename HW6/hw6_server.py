from socket import *
from collections import deque

BUFF_SIZE = 1024
port = 5555

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))

mbox = {}
while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    data = data.decode()

    if data == 'quit':
        break
    
    # 데이터 파싱
    data = data.split()
    t = data[0]
    mId = data[1]
    msg = data[2:]
    message = ' '.join(str(s) for s in msg)

    if t == 'send':                 # send일 때
        if mId not in mbox:         # 처음 mId를 사용하는 경우라면
            mbox[mId] = deque()     # 딕셔너리에 큐 생성
        mbox[mId].append(message)   # 메세지 큐에 추가
        s_sock.sendto('OK'.encode(), addr)
    elif t == 'receive':            # receive일 때
        if mId in mbox and len(mbox[mId]) != 0:     # 
            result = mbox[mId].popleft()
            s_sock.sendto(result.encode(), addr)
        else:
            s_sock.sendto('No messages'.encode(), addr)
    else:
        s_sock.sendto('Error!'.encode(), addr)
        break
