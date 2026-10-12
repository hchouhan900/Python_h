my_dict = {
    "name": "Anirudh",
    "age": 21,
    "gender": "Male",
}

print(my_dict)

# Method 1
# my_dict["xyz"] = 100 #Add and Update
# print(my_dict)

# Method 2
# my_dict["marks"] = 100
# my_dict["address"] = "Delhi"
# my_dict.update({"marks": 99, "address": "Delhi"})
del my_dict["gender"]
print(my_dict)
