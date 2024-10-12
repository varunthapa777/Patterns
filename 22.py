""" 
Enter n: 4
4444444
4333334
4322234
4321234
4322234
4333334
4444444
"""
n = int(input("Enter n: "))

for i in range(2*n-1):
    for j in range(2*n-1):
        top = i
        left = j
        right = (2*n-2)-j
        bottom = (2*n-2)-i
        print(n-min(top,left,right, bottom), end="")
    print()