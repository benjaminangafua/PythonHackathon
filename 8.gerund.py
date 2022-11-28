"""
Gerund

A gerund is the noun form of a verb that ends in -ing. For example, playing, dancing, eating.

TODO: Create a program that prompts users for a word and prints True if the word is a gerund, otherwise False.

Hint: https://docs.python.org/3/library/stdtypes.html#string-methods

Example 1:
Give me gerund: Chase
False

Example 2:
Give me a gerund: playing
True

Example 3:
Give me a gerund: DANCING
True
"""

# Get word from user
word = input("Give me a gerund: ").lower()

result = word.endswith("ing")

# print word
if result:
    print("True")
else:
    print("False")
    
print(result)

