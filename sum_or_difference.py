#Write a Python program that will return true if the two given integer
#values are equal or their sum or difference is 5.


a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))


if a == b or (a + b) == 5 or (a - b) == 5:
    print("True")
else:
    print("False")



