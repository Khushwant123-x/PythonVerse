n = int(input("Enter a number: "))

a = 0
b = 1

while b < n:
    a, b = b, a + b

if n == 0 or b == n:
    print("It is a Fibonacci number")
else:
    print("It is not a Fibonacci number")
