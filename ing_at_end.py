'''Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.'''

a=input("Enter a string:")

if len(a)>=3 and (a.endswith("ing")==False):
    print(a+"ing")
elif(a.endswith("ing")==True):
    print(a+"ly")
else:
    print(a)
