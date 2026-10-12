"""
user in input entering a number if present in list it will show the index value.
else it will show -1 if the number is not in the list entered by user.
"""

my_list = [34, 67, 89, 89, 56, 43, 100]

value = int(input("Enter value ="))

if value in my_list:  # iteration by using value.
    index = my_list.index(value)  # using index method
    print(f"Index={index}")
else:
    print(-1)


