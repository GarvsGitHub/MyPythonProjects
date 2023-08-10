# Constructing Objects and Accessing their Attributes and Methods
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

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
table.align["Pokemon Name"] = "l"
table.align["Type"] = "r"
print(table)
