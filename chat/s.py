from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.connect(('255.255.255.255', 3301))