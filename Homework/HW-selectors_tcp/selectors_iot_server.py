import selectors
from socket import *
import time
import sys

sel = selectors.DefaultSelector()       # 이벤츠 처리기 생성

def accept(sock,mask):                  # 새로운 클라이언트로부터 연결을 처리하는 함수
    conn, addr = sock.accept()  
    print('connected from ',addr)
    conn.send(b'register')
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)            # 소켓 연결 종료 시, 이벤트 처리기에서 등록 해제
        conn.close()
        return
    if data == b'quit':
        print(data.decode())
        f.close()
        sys.exit()
        
    write_txt(data.decode())

def write_txt(device):
    date = time.asctime()
    device_num = device[0]
    device_data = device[1:]
    result = str(date) + ": " + "Device" + device_num+ ": "+device_data
    f.write(result)
    print(result)

f = open('data.txt','w')

sock = socket()
sock.bind(('', 5555))
sock.listen(5)

# 서버 소켓을 이벤트 처리기에 등록
sel.register(sock, selectors.EVENT_READ, accept)
while True:
    events = sel.select()       # 등록된 객체에 대한 이벤트 감시 시작
    for key, mask in events:    # 발생한 이벤트를 모두 검사
        callback = key.data     # key.data: 이벤트 처리기에 등록한 callback 함수
        callback(key.fileobj, mask) # callback 함수 호출


