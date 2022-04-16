import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost',9000)
# connect는 tcp client에서만 함. (UDP client도 가능)
sock.connect(addr)

while True:
    message = input('Enter a message: ')

    if message == 'q':      
        break
    sock.send(message.encode())

    # 바이트 객체를 받아 문자열로 디코딩
    string = sock.recv(1024)       
    print(string.decode())

    # 바이트 객체를 받아 숫자로 변환
    byte_number = sock.recv(1024)  
    int_number = int.from_bytes(byte_number, 'big')
    print(int_number)

sock.close()