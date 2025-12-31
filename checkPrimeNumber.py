a=int(input("Enter a number:"))
if a<=1 :
    print("not a Prime Number")
flag=True
for i in range(2,a):
    if a%i==0:
        flag=False
        break
if flag:
    print("entered Number ia A Prime NUmber")
else: 
    print("not a Prime Number")       