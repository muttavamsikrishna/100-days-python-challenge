n=int(input('enter first number:'))
m=int(input('enter second number:'))
k=min(n,m)
for i in range(1,k+1):
    if (n%i==0 and m%i==0):
        gcd=i
print(gcd)
