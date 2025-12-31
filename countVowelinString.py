# Write a python program to count the vowels present in given input string. Explain the 
#output of program through example.

vowels=["a","e","i","o","u","A","E","I","O","U"]
s=" Write a python program to count the vowels present in given input string. Explain the" 
count=0
for ch in s:
    if ch in vowels:
        count+=1

print(f"total vowel in string s is {count}")
