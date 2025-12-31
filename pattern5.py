r=5
for i in range (r,0,-1):
    for j in range(r-i):
        print(" ",end=" ")
    for k in range (1,2*i):
        print("*",end=" ")
    print()