n=int(input('enter a number:'))
n1=int(input('enter starting multiple:'))
n2=int(input('enter last multiple:'))
if n2>n1:
   for i in range(n1,n2+1):
      print(n,' * ',i,' = ',n*i)
else:
   for i in range(n1,n2-1,-1):
      print(n,' * ',i,' = ',n*i)

   
