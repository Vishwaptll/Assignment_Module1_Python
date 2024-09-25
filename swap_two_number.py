#Write python program that swap two number with temp variable and without temp variable.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Before swapping:")
print("a :", a)
print("b :", b)
a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a :", a)
print("b :", b)
