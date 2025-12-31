def gen_fib(x):
    f=[]
    a,b=0,1
    for i in range (x):
        f.append(a)
        a,b=b,a+b
    return f

# Generate 10 fibnocci Number
print(gen_fib(10)) 


# generate fibnocci Number upto 100
def generatefib(x):
    f=[]
    a,b=0,1
    while a<=x:
        f.append(a)
        a,b=b,a+b
    return f

print(generatefib(100))  

# Recursive
def fibnocci(x):
  if x<=0:
     return 0
  elif x==1:
     return 1
  else:
     return fibnocci(x-1)+fibnocci(x-2)
for i in range (15):
   print(fibnocci(i),end=" ")
