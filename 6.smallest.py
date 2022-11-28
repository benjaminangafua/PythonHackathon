"""
Smallest

TODO: Write a python program that prompts users for three(3) numbers and prints out the smallest of the three.

ASSUME THAT THE NUMBERS USERS WILL PASS WILL BE DISTINCT/UNIQUE! NO REPETITION!

Example 1:

Number 1: 2
Number 2: 3
Number 3: 4

2

Example 2:

Number 1: 6
Number 2: 5
Number 3: 4

4
"""



num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

if num1 > num2 < num3:
    print(num2)
elif num1 > num3 < num2:
    print(num3)
else:
    print(num1)