n=int(input('enter starting range:'))
m=int(input('enter ending range:'))
import math
if n<m:
    for i in range(n,m+1):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
            print(i,'is prime')
elif n>m:
    for i in range(n,m-1,-1):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
            print(i,'is prime')
        
    
        
