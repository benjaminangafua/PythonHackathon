"""
Weekday

TODO: Write a program that prompts users for a number between 1 - 7 and prints out the name of the day of the week like 1 for Sunday, 2 for Monday and so on.

The program should not accept numbers other than 1 - 7.

Example 1:

Enter a number b/w 1 to 7: 2
Monday

Example 2:

Enter a number b/w 1 to 7: 8
Please enter a number b/w 1 to 7.
"""

number = int(input("Enter a number between 1 -7: "))

if 0< number <8:
    match number:
        case 1:
            print("Sunday")
        case  2:
            print("Monday")
        case  3:
            print("Tuesday")
        case  4:
            print("Wednesday")
        case  5:
            print("Thursday")
        case  6:
            print("Friday")
        case  7:
            print("Saturday")
        case _:
            print("Full Day")
else:
    print(f"You were to enter a positive number between 1 - 7 but you entered {number}")