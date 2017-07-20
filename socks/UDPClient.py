#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_DGRAM

port = 3300
name = 'HoHoHost'
sock = socket(AF_INET, SOCK_DGRAM)

data = input('Message: ')
sock.sendto(data, (name, port))
mod_data, server_address = sock.recvfrom(1024)

print(mod_data)

sock.close()