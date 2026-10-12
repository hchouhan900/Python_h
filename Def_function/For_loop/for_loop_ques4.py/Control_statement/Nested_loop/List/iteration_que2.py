"""
create a list of even "position" of list

"""

my_list = [3, 4, 6, "C&D", 887, 337, "Done"]

# Iterate by index
for i in range(0, len(my_list)):
    if i % 2 == 1:
        print(my_list[i], end=" ")




