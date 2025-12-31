# Construct a program that accepts a comma separated sequence of words as input and 
#prints the words in a comma-separated sequence after sorting them alphabetically.  
#Suppose the following input is supplied to the program: without, hello, bag, world  
#Then, the output should be: bag, hello, without, world 


words="without, hello, bag, world"

list=[word.strip() for word in words.split(",")]

list.sort()

sorted_words=", ".join(list)

print(f"sorted words={sorted_words}")

# Accept comma-separated words
words ="without, hello, bag, world"

# Split into list
words_list = [word.strip() for word in words.split(",")]

# Sort alphabetically
words_list.sort()

# Join back into comma-separated string
sorted_words = ", ".join(words_list)

print("Sorted words:", sorted_words)
