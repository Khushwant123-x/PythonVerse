n=int(input("enter number"))
def perfectaquare(x):
    for i in range (1,n):
        if(n==i**2):
            return n
    return -1     

result=perfectaquare(n)
if result==-1:
    print("not perfect square")
else:
    print(f"{n} is perfect square")    