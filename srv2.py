""" 
A simple echo server 
""" 

import socket 

host = '' 
port = 10000 
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
print ('The server is ready to receive')
while 1: 
    client, address = s.accept() 
    client.send(str.encode("Welcome to Captelizing Server"))
    data = client.recv(size) 
    if data:
	    message=data.decode("utf-8")
	    message=message.upper()
	    data=message.encode("utf-8")
	    client.send(data)
    client.close()