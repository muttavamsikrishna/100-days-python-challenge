n=int(input('enter first number:'))
m=int(input('enter second number:'))
def gc(a,b):
    if b==0:
        return a
    else:
        return gc(b,a%b)
lcm=n*m//gc(n,m)
print(lcm)
