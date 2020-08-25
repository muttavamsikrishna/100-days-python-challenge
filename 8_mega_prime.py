n=int(input('enter number:'))
import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
if prime(n):
    h=0
    while(n>0):
        r=n%10
        if prime(r):
            n=n//10
        else:
            h=1
            break
    if h==0:
        print('prime')
        print('mega prime')
    else:
        print('prime')
        print('not mega prime')
else:
    print('not prime')
    print('not mega prime')
