str1 = input("Entrer Odd string: ")

# middle_index = len(str1) // 2
# result = str1[middle_index - 1 : middle_index + 2]

# print("Middle three characters:", result)
# for i in range(0, -1, +1):
# str1 = input("Enter Odd string: ")

# Jab tak string ki length 3 se badi hai, aage aur peeche se ek-ek character hataate raho
while len(str1) > 3:
    # str1[1:-1] ka matlab hai: pehla aur aakhri letter chhod kar baaki sab le lo
    str1 = str1[1:-1]

print("Middle three characters:", str1)
