'''import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12345
s.bind((host,port))
s.listen(5)
while True:

    c, addr = s.accept()
    while True:
        n = input("enter n:")
        print('connection', addr)
        c.send(bytes(n, encoding='utf8'))
    # for i in range(10):
    #
    # c.close()'''




import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12345
s.bind((host,port))
s.listen(5)

while True:
    c, addr = s.accept()
    while True:

            n = input("enter n:")
            #print('connection', addr)
            c.send(bytes(n, encoding='utf8'))
            print("plz wait")
            print(c.recv(1024))




            #while True:




