"""
Voting.

TODO: Write a program that prompts users for their age and checks if the user is eligible to vote.

Example 1:

Age: 18
Eligible

Example 2:
Age: 17
Not eligible
"""

age = int(input("Enter your age e.g. 12: "))

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")