#!/usr/bin/env python3
# test5
import socket
import time

IP_ADDR = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP_ADDR, TCP_PORT))
s.listen(1)

while 1:
     conn, addr = s.accept()
     print('Client address:', addr)
     data = conn.recv(BUFFER_SIZE)
     #if not data: break
     currentTime = " " + " 2025년 7월 23일 수정함." + time.ctime(time.time()) + "\r\n"
     print(data.decode('utf-8'))
     data = data + currentTime.encode('utf-8')
     conn.send(data)  # echo
     print('Data sent back to client:', data.decode('utf-8'))
     time.sleep(1)  # 1초 대기
     conn.close()
