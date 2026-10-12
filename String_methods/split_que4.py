"""
Write a program that converts a string in camel case to snake_case.

"""

my_string = "helloWorldHowAreYou"

result = ""  # Yeh ek khali dabba hai jisme hum naya word banayenge

for char in my_string:  # Ek-ek karke sabhi letters ko check kar rahe hain

    if char.isupper():  # Kya yeh letter bada (capital) hai?
        result = (
            result + "_" + char.lower()
        )  # Agar haan, toh underscore aur chhota letter jod do

    else:  # Agar bada nahi hai (chhota hai)
        result = result + char  # Toh waisa ka waisa jod do

print(result)  # Output aayega: hello_world
