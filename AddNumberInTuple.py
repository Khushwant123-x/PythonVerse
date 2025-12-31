# Method 1
a=(1,2,3,4)
l=list(a)
l.append(58)
a=tuple(l)
print(a)
# Method 2
a=a+(67,)
print(a)