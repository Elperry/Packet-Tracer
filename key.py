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
    return numOfOnes
