n=int(input('enter range:'))
for i in range(n):
    print(('* '*(i+1)).center(2*n))
for i in range(n-2,-1,-1):
    print(('* '*(i+1)).center(2*n))
