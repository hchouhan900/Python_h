"""
Ask a string from user.Convert all the alphabets to uppertcase.
"""

# my_string = input("Enter any string = ")
# result = my_string.upper()
# print(result)

# for ch in my_string:
#     if ch.islower( ):
#         print(ch.isupper) #it will be result+=ch.upper()
#     else:
#         print(my_string)    #it will be not a print it will be "result+=ch"
  
my_string = input("Enter any string = ")
result = ""

for ch in my_string:
    if ch.islower():
        result += ch.upper()
    else:
        result += ch
                                        
print(result)
