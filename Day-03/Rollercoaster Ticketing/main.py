
print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the roller-coaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket's are $5")
    elif age < 18:
        bill = 7
        print("Youth ticket's are $7")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult ticket's are $12")

    photo = input("Do you want to take photos? Y/N ->")
    if photo == "Y":
        bill += 3
        print(f"Please pay ${bill}")
    else:
        print(f"Please pay ${bill}")
else:
    print("Sorry, you have to grow taller to ride this.")
