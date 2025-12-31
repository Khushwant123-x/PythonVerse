#Write a Python function removekth(s, k) that takes as input a string s and an integer k>=0 
#and removes the character at index k. If k is beyond the length of s, the whole of s is 
#returned. For example,  
#emovekth(“PYTHON”, 1) returns “PTHON”  
#removekth(“PYTHON”, 3) returns “PYTON”  
#removekth(“PYTHON”, 0) returns “YTHON”  
#removekth(“PYTHON”, 20) returns “PYTHON” 

def removekth(s, k):
    if k >= len(s):
        return s
    return s[:k] + s[k+1:]

print(removekth("PYTHON", 1))
print(removekth("PYTHON", 3))
print(removekth("PYTHON", 0))
print(removekth("PYTHON", 20))




