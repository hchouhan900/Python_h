"""
Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 to the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.
"""

list_m = [100, 50, 400, 500]

# 1. Change the second element (index 1) to 200 and print
# my_list[1] = 200
# print("After Change:", my_list)

# # 2. Add 600 to the end of the list and print
# # my_list.append(600)
# my_list.append(600)
# print("After Append:", my_list)

# # 3. Insert 300 at the third position (index 2) and print
# # my_list.insert(2, 300) 
# my_list.insert(2,300)
# print("Afrter Insert:",my_list)

# # 4. Remove 600 from the list by value and print
# my_list.remove(600)
# print("After Remove by Value:", my_list)

# # 5. Remove the element at index 0 and print
# my_list.pop(0)  # Alternatively: del my_list[0]
# print("After Remove by Index:", my_list)
# my_list.append(600)
# print("After append:",my_list)

# my_list.remove(600)
# print("After Remove:",my_list)

# my_list.insert(2,300)
# print("After Insert:",my_list)


list_m[1] = 200
print(f"Updated (Change): {list_m}")

# b) Append Element
list_m.append(600)
print(f"Updated (Append): {list_m}")

# c) Insert Element
list_m.insert(2, 300)
print(f"Updated (Insert): {list_m}")

# d) Remove Element by value
list_m.remove(600)
print(f"Updated (Remove 600): {list_m}")

# e) Remove Element by index
list_m.pop(0)
print(f"Updated (Remove Index 0): {list_m}")        
