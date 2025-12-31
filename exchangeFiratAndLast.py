#Write a Python program to change a given string to a new string where the first and last 
#chars have been exchanged.

def exchange(s):
    if len(s)<=1:
        return s
    return s[-1]+s[1:-1]+s[0]

s="PYTHON"
print(exchange(s))