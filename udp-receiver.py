import socket
import time
import myPublicIp

UDP_IP = "0.0.0.0"
UDP_PORT = 5001

# update in 20240809 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

print("20240809 Computer Network: Azure cloud testing ! A UDP server started !")
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("Received message:", data.decode('utf8'), " from ", addr)
    currentTime = " " + time.ctime(time.time()) + "\r\n"
    my_ip = myPublicIp.getPublicIp()
    data = "MS Azure cloud server ".encode('ascii') + my_ip.encode('ascii')  + " ".encode('ascii') + data + currentTime.encode('ascii')
    sock.sendto(data, addr)
