'''
Instructions
You are going to write a program that will select a random name from a list of names. The person selected will have to
pay for everybody's food bill.

Important: You are not allowed to use the choice() function.
'''

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")  # It gives output in list format

size = len(names)
name = names[random.randint(0, size-1)]
print(name + " is going to buy the meal today!")
