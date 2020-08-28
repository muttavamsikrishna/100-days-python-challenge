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
if prime(n):
    h=n
    a=getprevprime(n)
    b=getprevprime(a)
    while(b>2):
        if a+b+1==h:
            print('special prime')
            print('{}+{}+1={}'.format(a,b,h))
            break
        a=b
        b=getprevprime(a)
    else:
        print('prime but not special prime')
else:
    print('not prime')
    
    
