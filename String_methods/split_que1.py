"""
Write a program to reverse the order of words
"""

my_string = "python is good"
words = my_string.split() #split will make it in a list form

words = words[::-1] #it will do a reverse of the list

result = " ".join(words) #it will join the list and forma a word

print(result)
