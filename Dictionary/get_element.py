my_dict = {
    "name": "Anirudh",
    "age": 21,
    "gender": "Male",
}

# print(my_dict["name"])
# print(my_dict["age"])

# to get value
# r=my_dict.get("name")
# print(r)

k = input("Enter a key = ")
result = my_dict.get(k)

if result is not None:
    print(result)
else:
    print("key does not exist")
