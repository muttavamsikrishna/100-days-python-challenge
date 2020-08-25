import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input('enter number:'))
for i in range(n-1,1,-1):
    if prime(i):
        print(i)
        break
while(n>1):
    if prime(n):
        print(n)
        break
    n=n+1
    
