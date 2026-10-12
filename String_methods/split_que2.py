"""
Write a program to make every first letter to be in capital(Upper Case)
"""
my_string = "python is good"
words = my_string.split()

result=" ".join(i.capitalize() for i in words)

print(result)
