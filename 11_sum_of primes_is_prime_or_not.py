import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input('enter a number:'))
def getprevprime(n): 
    for i in range(n-1,0,-1):
        if prime(i):
            return i
            break
if prime(n):
    h=n
    a=getprevprime(n)
    b=getprevprime(a)
    while(a>=2):
        while(b>=2):
            if a+b==h:
                print('sum of ',a,'+',b,'is =',a+b)
                break
            b=getprevprime(b)
        a=getprevprime(a)
        b=getprevprime(a)
else:
    print('not prime')


    
    
    
