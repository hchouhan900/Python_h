"""
Find the upper and lower alphabets in a string
"""

my_string = "abc123ABCD"
lower_count = 0
upper_count = 0

# for ch in my_string:
#     if ch.isupper():
#         upper_count += 1
#     elif ch.islower():
#         lower_count += 1

for ch in my_string:
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90: #ascii codes are there for the alphabets that are given in a google
        upper_count += 1
    elif ascii >= 97 and ascii <= 122:
        lower_count += 1

print(upper_count)
print(lower_count)
