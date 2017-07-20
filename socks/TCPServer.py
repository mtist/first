from socket import socket, AF_INET, SOCK_STREAM

port = 3300
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

while True:
    con_sock, address = sock.accept()
    data = con_sock.recv(1024)
    data = data.decode('utf-8')
    udata = data.upper()
    udata = udata.encode('utf-8')
    con_sock.send(udata)
    con_sock.close()