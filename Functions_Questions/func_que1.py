"""
Write a function that accepts an integer and prints the
multiplication table fotr that number upto 10
 5
 5 x 1 = 5
 5 x 2 =10
 ...
"""


def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i}={num*i}")


multiplication_table(8)
