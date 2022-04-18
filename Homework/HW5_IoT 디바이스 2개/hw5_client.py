import socket
import time

BUFF_SIZE = 1024
port1 = 5555
port2 = 6666

f = open('data.txt','w')

def write_txt(device, data):
    date = time.strftime('%c', time.localtime(time.time()))
    result = str(date) + ": " + "Device" + device + ": "+data
    f.write(result)
    
while True:
    d1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    d1_addr = ('localhost',port1)
    d1.connect(d1_addr)
    
    d2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    d2_addr = ('localhost',port2)
    d2.connect(d2_addr)

    msg = input("Entet the number: ")

    if msg == '1':
        d1.send(msg.encode())
        data1 = d1.recv(1024).decode()
        write_txt('1',data1)
    elif msg == '2':
        d2.send(msg.encode())
        data2 = d2.recv(1024).decode()
        write_txt('2',data2)
    elif msg == 'quit':
        d1.send(msg.encode())
        d2.send(msg.encode())
        d1.close()
        d2.close()
        f.close()
        break
          
d1.close()
d2.close()
