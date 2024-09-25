#Write a Python function that takes a list of words and returns the length of the longest one.


a = input("Enter a list of words separated by spaces: ").split()
if not a:
    longest_length = 0
else:
    
    b= max(len(word) for word in a)


print("Length of the longest word:", b)
