import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr = s.accept()
    while True:
        try:
            input = client.recv(1024)
            input = input.decode()
        except:
            break
        else:
            if not input:
                break

        a, oper, b = input.split()
        a = int(a)
        b = int(b)

        if oper == '+':
            result = a + b
        elif oper == '-':
            result = a - b
        elif oper == '*' :
            result = a * b
        elif oper == '/':
            result = round(a / b, 1)

        client.send(str(result).encode())

    client.close()