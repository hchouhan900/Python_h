"""
Write a function that takes a string and prints whether it is a
palindrome.

mom
"""


def check_palindrome(strings):
    if strings == strings[::-1]:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")


check_palindrome("mom")
check_palindrome("abcdef")
