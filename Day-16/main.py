# ===== Constructing Objects and Accessing their Attributes and Methods ===== #

# ===== Working on inbuilt turtle graphic package ===== #
# from turtle import Turtle, Screen
#
# kurma = Turtle()  # Created object named kurma and assigned blueprint(class) to it
# print(kurma)
# kurma.color("Green")  # Used methods of that class
# kurma.shape("turtle")
# kurma.forward(100)
#
# my_screen = Screen()  # Similarly created object of Screen class
# print(my_screen.canvheight)  # Used attribute of class i.e. my_screen.canvheight
# my_screen.exitonclick()


# ===== Working on downloaded package of prettytable ==== #
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])  # .add_column("Fieldname_of_Table", ["Attributes in the field"]
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"  # For entire table(l=left)
table.align["Pokemon Name"] = "l"  # For a specific field(r=right) 
table.align["Type"] = "r"
print(table)
