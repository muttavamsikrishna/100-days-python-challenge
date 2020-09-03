n=int(input('enter number:'))
a=0
b=1
c=0
sum=1
for i in range(n-2):
    if n<=c:
        if n==c:
            print(c)
            break
        else:
            print(a)
            break
    c=(a+b)
    sum=sum+c
    #print(c,end=' ')
    a,b=b,c
   
    
