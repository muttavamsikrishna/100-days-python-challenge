n=int(input('enter number:'))
k=str(n)
h=0
for i in range(len(k)-1):
    if int(k[i])==int(k[i+1])+1:
        h=1
    elif int(k[i])==int(k[i+1])-1:
        h=-1
    else:
        h=0
        break
if h==-1:
    print('ascending')
elif h==1:
    print('decending')
else:
    print('no format')
    
