"""Construct a function perfect_square(number) that returns a number if it is a perfect 
square otherwise it returns -1.  
For example:  
perfect_square(1) returns 1  
perfect_square (2) returns -1 """

def perfect_square(n):
    for i in range(1,n+1):
        if i**2==n:
            return 1
    return -1

perfect_square(1)
perfect_square(4)
perfect_square(2)
perfect_square(6)