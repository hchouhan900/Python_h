"""
print th number that is bigger than largest in the list
"""

my_list = [3, 4, 6, 100, 887, 337, 10]

largest = 0
# Iterate by index
for i in range(0, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
