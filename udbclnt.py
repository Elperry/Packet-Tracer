import socket
import numpy as np

#Key function
dictionary=[]
for i in range(255):
    c=chr(i)
    dictionary.append(c)

def onesCounter(string):
    numOfOnes=0
    for c in string:
        i=dictionary.index('A')
        b=bin(i)
        numOfOnes += b.count('1')
    return '{0:03}'.format(numOfOnes)
#end of key fn
#devide the message and add the header
def constructPackets(message,size=50):
    l=len(message)
    packets = []
    i=0
    n=0
    while(i < l):
        p='{0:02}'.format(n)+onesCounter(message[i:i+size])+message[i:i+size]
        packets.append(p)
        i+=size
        n +=1
    return packets
#end of fn
# reliableSender function
def reliableSender(packets):
    for p in packets:
        flag = True;
        while (flag):
            clientSocket.sendto(p.encode('UTF-8'),(serverName, serverPort))
            try:
                data, clientAddress = clientSocket.recvfrom(2048)
                if(int(data)==200):
                    print("packet sent")
                    flag=False
            except Exception as e:
                print("no receive")

# end sender
serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = input('Input lowercase sentence: ')
packets = constructPackets(message,50)
reliableSender(packets)

clientSocket.close()
message=input('Press enter to exit')
