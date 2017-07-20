#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_DGRAM

port = 3300
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, caddress = sock.recvfrom(1024)
    sock.sendto(data.upper(), caddress)


