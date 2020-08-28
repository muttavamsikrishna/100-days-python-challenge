import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input('enter a number'))
def getprevprime(n): 
    for i in range(n-1,1,-1):
        if prime(i):
            return i
            break
if prime(n):
    h=n
    k=list()
    k.append(n)
    while(n>2):
        n=getprevprime(n)
        k.append(n)
    k.reverse()
    if prime(k.index(h)+1):
        print('super prime')
    else:
        print('prime but not super prime')
    
    
else:
    print('not prime')
    
    
