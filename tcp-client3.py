#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import socket

#IP = '127.0.0.1'
IP = '3.34.178.210'
#IP = '168.188.126.81'
TCP_PORT = 54147
BUFFER_SIZE = 1024
MESSAGE = '안녕'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, TCP_PORT))

while True:
    MESSAGE = input()
    if MESSAGE == "q":
        break
    print("Sending")
    s.send(MESSAGE.encode('utf-8'))
    data = s.recv(BUFFER_SIZE)
    print(data.decode('utf-8'))
    print(len(data))
    if len(data) == 0:
        break

s.close()
