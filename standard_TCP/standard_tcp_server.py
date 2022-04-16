import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr = s.accept()       # 클라이언트 연결 수락
    print('Connection from ', addr) 

    # 바이트 객체 데이터 받아서 디코딩
    msg = client.recv(1024).decode()
    if not msg:
        s.close()
        sys.exit()      # 이중루프거나 종료해야할 때 사용
    elif msg == 'q':
        break
    print(msg)

    # 문자열을 바이트 객체로 변환하여 전송
    client.send(b'send string')   

    # 숫자를 바이트 객체로 변환하여 전송
    # msg를 4바이트의 빅 엔디안으로 변환하여 전송해라
    msg = 12345                          
    client.send(msg.to_bytes(4, 'big'))  

client.close()
s.close()