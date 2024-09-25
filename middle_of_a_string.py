#Write a Python function to insert a string in the middle of a string


a1= input("Enter the first string: ")
a2= input("Enter the string to insert in middle: ") 


middle_index = len(a1)


final= a1[:middle_index] + a2 + a1[middle_index:]


print("String:", final)





