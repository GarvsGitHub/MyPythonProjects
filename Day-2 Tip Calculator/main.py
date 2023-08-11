# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total Bill? $")
tip = input("What percentage tip would you like to give?\n10, 12 or 15?\n")
split = input("How many to split the Bill? ")
bill_with_tip = int(total_bill) + (int(total_bill) * int(tip) / 100)
final_bill = bill_with_tip / int(split)
print(f"Each person should pay: ${round(final_bill,2)}")
