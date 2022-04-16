from socket import *

port = 2500

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print('connected IP:', remotehost, "port:",remoteport)

msg = "simple TCP code."
conn.send(msg.encode())

conn.close()
sock.close()