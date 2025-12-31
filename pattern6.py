r=4
for i in range(1,r+1):
    for j in range(r-i):
        print(" ",end=" ")
    for k in range (1,2*i):
        print("*",end=" ")
    print()

for i in range(r-1,0,-1):
    for j in range(r-i):
        print(" ",end=" ")
    for k in range (1,2*i):
        print("*",end=" ")
    print()