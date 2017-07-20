from socket import socket, AF_INET, SOCK_STREAM

serv_name = '192.168.7.104'
port = 3300
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((serv_name, port))

data = input('Message: ').encode('utf-8')
sock.send(data)
udata = sock.recv(1024).decode('utf-8')
print(udata)
sock.close()