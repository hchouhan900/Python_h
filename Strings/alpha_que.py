"""
How many alphabets are there in a string
"""

my_string = "abc123"
count = 0
for ch in my_string:
    if ch.isalpha():
        count = count + 1

print(count)
