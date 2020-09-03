n=int(input('enter number:'))
def getprevfib(n):
    a=0
    b=1
    while(n>=b):
        a,b=b,a+b
    return a
def fib(n):
    a=0
    b=1
    for i in range(n+1):
        a,b=b,a+b
        if a==n:
            return True
    else:
        return False
l=list()
if fib(n):
        print(n,' is fibonacci element')
else:
    while(n>0):
        k=getprevfib(n)
        l.append(k)
        h=n-k
        if fib(h):
            print('it has sum of fibonacci elements')
            for i in l:
                print(i,end=' ')
            print(h)
            #print(h)
            break
        else:
            n=h
    else:
        print('it cant be sum of fibonacci elements')
    
