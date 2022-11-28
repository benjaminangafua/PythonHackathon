"""
Grading

TODO: Doe Community High School has following rules for grading students:

96 to 100 - A+
90 to 95  - A
80 to 89  - B
70 to 79  - C
Below 70  - F

Write a function named getGrade that prompts users for their score and prints their corresponding grade.

Example 1:

getGrade(91)
A

Example 2:

getGrade(69)
F
"""

def main():

    grade = int(input("Enter grade: "))
    getGrade(grade)

def getGrade(gd):

    if 95<gd<1001:
        print("A+")
    elif 89<gd<96:
        print("A")
    elif 79<gd<90:
        print("B")
    elif 69<gd<80:
        print("C")
    elif gd < 70:
        print("F")
    else:
        print("INC")
main()