n=int(input('enter range:'))
a=0
b=1
c=0
sum=1
print(a,b,sep=' ',end=' ')
for i in range(n-2):
    c=(a+b)
    sum=sum+c
    print(c,end=' ')
    a,b=b,c
print()
print('n th elemeny of fibonacci series:',c)
print('sum of fibonacci series:',sum)
   
   
    
