# Program to capitalize lines of input

lines = []

print("Enter lines of text (type 'STOP' to end):")

while True:
    line = input()
    if line.upper() == "STOP":
        break
    lines.append(line)

print("\nLines in uppercase:")
for line in lines:
    print(line.upper())
