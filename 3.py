"""
    1
    12
    123
    1234
    12345
"""

n = int(input("Enter n: "))

for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    print()