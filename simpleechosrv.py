""" 
A simple echo server 
""" 

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    print ('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print ('client connected:', client_address)
        while True:
            data = connection.recv(16)
            print ('received "%s"' % data.decode("utf-8"))
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()