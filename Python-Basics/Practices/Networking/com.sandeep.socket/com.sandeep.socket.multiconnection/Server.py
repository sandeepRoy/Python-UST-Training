# server
import socket
s = socket.socket()
print("socket created")
s.bind(('localhost',1234))
s.listen(3)
print("waiting for connections")
while True:
    c, addr = s.accept() #it returns for address and client socket
    name=c.recv(1024).decode()
    print("connected with client", addr,name)
    c.send(bytes("welcome to python socket",'utf-8'))
    c.close()