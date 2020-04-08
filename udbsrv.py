import socket

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
    return str(numOfOnes)
#end of key fn

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
message=[]
ack='200'
while 1:
    data, clientAddress = serverSocket.recvfrom(2048)
    try:
        pa=data.decode("UTF-8")
        vKey=int(pa[2:5])
        calculatedKey=int(onesCounter(pa[5:]))
        # cheking for the error
        if(vKey == calculatedKey ):
            # send ayah number
            serverSocket.sendto(ack.encode("UTF-8"), clientAddress)
            print (pa[5:])
    except Exception as e:
        print(e)
