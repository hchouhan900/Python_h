"""
Write a python code to find  the occurence  of each elemrnt in a list and
print the element with the highest occurence.
"""

my_list = [5, 1, "Code and  Debug", 56.32, 5, "Anirudh", 1, 1, "Aniirudh"]
result = []

for num in my_list:
    if num not in result:
        result.append(num)

highest_occ_element = 0
highest_occurence = 0

for num in result:
    c = my_list.count(num)
    print(f"{num} occurs {c} times")
    if c > highest_occurence:
        highest_occurence = c
        highest_occ_element = num

print(f"Highest occurent element={highest_occ_element}")
