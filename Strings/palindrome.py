"""
palindrome program to check wheather the word is palindrome or not
mom
noon
"""

my_string = input("Entert a string = ")

if my_string == my_string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
