from socket import *

server = create_server(('', 9000))
conn, addr = server.accept()

conn.send(b'This is IoT world!')
conn.close()