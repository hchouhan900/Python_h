"""
Write a function that accepts a string and prints 
the frequency of each character in the string.

hello
h occurs 1 time
e occurs 1 time
l occurs 2 times
o occurs 1 time
"""


def charCount(string):
    # my_dict={}
    my_dict = dict()                         
    for ch in string:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1
    for k, v in my_dict.items():
        print(f"{k} occurs {v} times")


charCount("aaabccddddef")
