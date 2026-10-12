"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3 
n n n n n
"""

n=int(input("Enter number of lines = "))
for i in range(n,0,-1):
    for j in range(1,6):
        print(i,end=" ")
    print()