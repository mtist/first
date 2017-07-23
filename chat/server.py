from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
host = ''
address = '255.255.255.0'
port = 2200
s.bind((host, port))
s.connect((address, port))
s.listen(10)

while True:
        
        c, addr = s.accept()
        print ('Got connection from', addr)