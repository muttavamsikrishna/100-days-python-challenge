n=int(input('enter number:'))
a=0
b=1
while(n>=b):
    a,b=b,a+b
if abs(a-n)<=abs(b-n):
    print(a)
else:
    print(b)
