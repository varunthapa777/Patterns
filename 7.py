""" 
    *
   ***
  *****
 *******
*********
"""

n = int(input("Enter n: "))
for i in range(n):
        a = 2*i + 1
        print(" "*(n-i-1),end="")
        print("*"*a)