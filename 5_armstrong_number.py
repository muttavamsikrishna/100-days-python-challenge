n=int(input('enter a number:'))
l=n
sum=0
while(n>0):
    r=n%10
    sum=sum+r**3
    n=n//10
if sum==l:
    print('armstrong')
else:
    print('not armstrong')
