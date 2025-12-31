#Write a function to find the longest word in a given list of words. Example: 
#longest_word([‘apple’, ‘banana’, ‘cherry’]) returns ‘banana’.

def longest_word(lst):
    longest=""
    for word in lst:
        if len(word)>len(longest):
            longest=word
    return longest
print(longest_word(['apple', 'banana', 'cherry']))
        