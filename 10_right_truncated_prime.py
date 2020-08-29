import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input('enter a number:'))
def getprevprime(n): 
    for i in range(n-1,1,-1):
        if prime(i):
            return i
            break
k=0
if prime(n):
    n=n//10
    while prime(n) and n>0:
        n=n//10
        if prime(n):
            k=1
        else:
            k=0
else:
    print('not prime')
if (k==1):
    print('right truncated prime')
else:
    print('not right truncated prime')
    
    
