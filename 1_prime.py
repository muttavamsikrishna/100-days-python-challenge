n=int(input())
import math
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        print('not prime')
        break
else:
    print('prime')
