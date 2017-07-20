#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_DGRAM

port = 3300
name = '192.168.7.104'
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('Message: ')
    udata = data.encode('utf-8')
    sock.sendto(udata, (name, port))
    mod_data, server_address = sock.recvfrom(1024)
    mod_data = mod_data.decode('utf-8')
    print(mod_data)

sock.close()