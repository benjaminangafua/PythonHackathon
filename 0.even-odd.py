"""
Even-Odd

TODO: Write a program to check whether a number entered by a user is even or odd.

Example 1:

Number: 20
Even

Example 2:

Number: 7
Odd
"""

number = int(input("Enter a number: "))

if number%2==0:
    print("Even")
else:
    print("Odd")