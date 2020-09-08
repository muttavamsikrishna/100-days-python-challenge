n=int(input('enter number:'))
def even(n):
    if n%2==0:
        return True
    else:
        return False
print(n,end=' ')
while(n>1):
    if even(n):
        n=n//2
        print(n,end=' ')
    else:
        n=n*3+1
        print(n,end=' ')

    
    
    
