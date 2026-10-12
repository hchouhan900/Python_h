"""
Write a program that prompts the user to specify the length of a list and then requests a number to populate  that list.display the final list as the output.
"""

# list_length=int(input("Enter length ="))
# result= []

# for i in range(0,list_length):
#     num=int(input("Enter number ="))
#     result.append(num)

# print(result)

list_length = int(input("Enter length ="))
result = []  # store list in this result

for i in range(0, list_length):  # the input from user from 0 to user wants to get the required number.
    num = int(input("Enter number ="))  # taking input from user about the list.
    result.append(num)  # add the number to result empty list.

print(result)
