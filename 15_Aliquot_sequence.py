n=int(input('enter number:'))
def factor(n):
    sum=0
    for i in range(n//2,0,-1):
        if n%i==0:
            sum+=i
    return sum
print(n,end=' ')
while(n>1):
    h=factor(n)
    if h==n:
        break
    else:
        print(h,end=' ')
        n=h
    

