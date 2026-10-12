"""
Write a python program to check if two given sets have no elements
in common.
"""

set1 = {5, 6, 2, 1, "Anirudh", 7}
set2 = {"Python", 76, 22, 91, -991, 1}

result = set1.intersection(set2)

if len(result) == 0:
    print("Both sets have nothing in common")
else:
    print("Both sets have something in common")
    print(result)
