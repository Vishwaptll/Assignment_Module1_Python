#Write a python program to sum of the first n positive integers.


n = int(input("Enter a positive integer n: "))


if n > 0:
    total = sum(range(1, n + 1))
    print("The sum of the first", n, "positive integers is:", total)
else:
    print("Please enter a positive integer.....")

