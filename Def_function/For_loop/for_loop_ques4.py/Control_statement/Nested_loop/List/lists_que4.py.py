"""
write a list of your own .And remove all the duplicate element from that list.
"""

my_list = [5, 1, "Code and Debug", 56.32, 5, 5, "Anirudh", 1, 1, "Anirudh"]
result = []

for num in my_list:
    if num not in result:
        result.append(num)

print(result)
