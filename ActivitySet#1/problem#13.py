# Network Programming
# https://www.py4e.com/lessons/network

#def f(*args,**kwags):
  #print(args,*args,kwags,)#**kwags)
#f(1,2,3,a=10,b=20)
import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b"" 

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())
(
fhand.write(picture)
fhand.close()