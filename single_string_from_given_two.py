#Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.

a = input("Enter the first string: ")
b = input("Enter the second string: ")

x=b[:2]+a[2:]
y=a[:2]+b[2:]

a1=(x+" "+y)
print("String :",a1)
