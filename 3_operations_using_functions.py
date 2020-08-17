a,b=map(int,input('enter two numbers:').split())
def add(a,b):
   multiply(a,b)
   print('adiition:',a+b)
def multiply(a,b):
   div(a,b)
   print('multiplication:',a*b)
def div(a,b):
   sub(a,b)
   print('division:',a/b)
def sub(a,b):
   print('subtraction:',a-b)
add(a,b)
