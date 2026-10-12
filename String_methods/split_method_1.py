# a = "hello world this is python"
# words = a.split()

# print(words)
# a = "hello-world-this-is-python"
# words = a.split("-")

# print(words)
my_list = ["abc", "anirudh", "xyz", "hello"]

# my_string = " ".join(my_list)
my_string = " ".join(i for i in my_list)
print(my_string)
print(type(my_string))
