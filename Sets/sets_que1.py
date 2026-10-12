"""
Given two lists a,b. Check if two lists have atleast one element
common in them.
"""

lst1 = [3, 6, 7, 5, 55, 3, 1, 2, 2, "Python", "Anirudh"]
lst2 = [7, 8, 5, 6, 1, "Anirudh"]

print(set(lst1) & set(lst2)) #most simple method
# set1 = set(lst1)
# set2 = set(lst2)

# print(set1.intersection(set2))
# print(set1 & set2)  #for intersection we use &
# print(set1 | set2) #for union we use |
