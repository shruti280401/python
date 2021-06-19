
import socket
s=socket.socket()
host=socket.gethostname()
port=12345
#s.connect(('192.168.0.107',12345))
s.connect((host,port))
while True:
                print(s.recv(1024))
                #c, addr = s.accept()
                n=input("enter n:")
                #print('connection', addr)
                s.send(bytes(n, encoding='utf8'))
                print("plz wait")


