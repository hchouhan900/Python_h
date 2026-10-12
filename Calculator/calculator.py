a=int(input("Enter any number="))
b=int(input("Enter any number="))
op=input("Enter operator(+,-,*,/):")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
elif op == "**":
    print(a**b)
else :
    print("Invalid Operation")