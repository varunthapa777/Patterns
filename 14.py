""" 
A
AB
ABC
ABCD
ABCDE
"""
n = int(input("Enter n: "))
a = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(a+j), end="")
    print()