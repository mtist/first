import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while 1:
    # sock.sendto('broadcast!'.encode('utf-8'), ('255.255.255.255',11719))
    sock.connect(('255.255.255.255', 3301))
    print('Nice!')