from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')[0]
    words = req.split()
    filename = words[1][1:]

    if filename == 'index.html':
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: '+str(mimeType).encode()+b'\r\n')
        c.send(b'\r\n')
        c.send(f.read().encode('euc-kr'))

    elif filename == 'iot.png':
        f = open(filename, 'rb')
        mimeType = 'image/png'

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: '+str(mimeType).encode()+b'\r\n')
        c.send(b'\r\n')
        c.send(f.read())

    elif filename == 'favicon.ico':
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: '+str(mimeType).encode()+b'\r\n')
        c.send(b'\r\n')
        c.send(f.read())

    else:
        c.send(b'HTTP/1.1 404 NOT FOUND\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')

    c.close() 