"""
Write Replace old number from new and taking input from the user.

"""

# my_list=[56,78,21,34,99,56,21,24]
# old=int(input("Enter old number="))
# new=int(input("Enter new number="))
# for i in range(0, len(my_list)):
#     if my_list[i] == old:
#         my_list[i] = new

# print(my_list)

my_list = [56, 90, 50, 21, 21, 34, 21, 30, 21]
old = int(input("Enter old number="))
new = int(input("Enter new number="))

for i in range(0, len(my_list)):
    if my_list[i] == old:
        my_list[i] = new

print(my_list)
