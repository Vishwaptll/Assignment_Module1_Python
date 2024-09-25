# Write a Python program to get the Fibonacci series of given range.


n = int(input("Enter the number of terms in the Fibonacci series: "))


a, b = 0, 1


print("Fibonacci series:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b  
