n=int(input('enter number:'))
def number(n,l):
    sum=0
    k=n
    while(n>0):
        r=n%10
        sum=sum+r**l
        n=n//10
    if k==sum:
        return True
    else:
        return False
def length(n):
    sum=0
    while(n>0):
        sum+=1
        n=n//10
    return sum
l=length(n)
print(l)
print(number(n,l))
    

