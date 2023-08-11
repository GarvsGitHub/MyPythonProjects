# In this simple Boxed Map you decide in which box to put the treasure.
# Input eg: 23, In this input 2 is row & 3 is column.
# [11, 12, 13]
# [21, 22, 23]
# [31, 32, 33]
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
mapp = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row = int(position[0])-1
col = int(position[1])-1
mapp[row][col] = "X "

print(f"{row1}\n{row2}\n{row3}")
