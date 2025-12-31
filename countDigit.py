# Write a program that accepts a sentence and calculate the number of digits.

s="Khushwant has 10 pairs shoes.Khushwant has 22 cars.My phone number is 98765"

def countDigit(s):
    count=0
    for ch in s:
        if ch.isdigit():
            count+=1
    return count

print(countDigit(s))