# ===== Data give in the form of Dictionary ===== #
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# ===== Code starts here ===== #
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
balance = 0


def report_function():
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${balance}")


def check_resources(p, w, m, c):
    if p == 'espresso':
        es_water = MENU["espresso"]["ingredients"]["water"]
        es_coffee = MENU["espresso"]["ingredients"]["coffee"]
        w -= es_water
        c -= es_coffee
        if w < 0 and c < 0:
            return "water and coffee"
        elif w < 0:
            return "water"
        elif c < 0:
            return "coffee"
        else:
            return "True"
    elif p == 'latte':
        la_water = MENU["latte"]["ingredients"]["water"]
        la_milk = MENU["latte"]["ingredients"]["milk"]
        la_coffee = MENU["latte"]["ingredients"]["coffee"]
        w -= la_water
        m -= la_milk
        c -= la_coffee
        if w < 0 and m < 0 and c < 0:
            return "water, milk and coffee"
        elif w < 0 and c < 0:
            return "water and coffee"
        elif w < 0:
            return "water"
        elif c < 0:
            return "coffee"
        else:
            return "True"
    else:
        ca_water = MENU["cappuccino"]["ingredients"]["water"]
        ca_milk = MENU["cappuccino"]["ingredients"]["milk"]
        ca_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        w -= ca_water
        m -= ca_milk
        c -= ca_coffee
        if w < 0 and m < 0 and c < 0:
            return "water, milk and coffee"
        elif w < 0 and c < 0:
            return "water and coffee"
        elif w < 0:
            return "water"
        elif c < 0:
            return "coffee"
        else:
            return "True"


def money(p):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    paid = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies

    if p == 'espresso':
        cost = MENU["espresso"]["cost"]
        if cost > paid:
            print("Sorry that's not enough money, Money refunded.")
            return False
        elif cost < paid:
            change = round((paid - cost), 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            return True
    elif p == 'latte':
        cost = MENU["latte"]["cost"]
        if cost > paid:
            print("Sorry that's not enough money, Money refunded.")
            return False
        elif cost < paid:
            change = round((paid - cost), 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            return True
    else:
        cost = MENU["cappuccino"]["cost"]
        if cost > paid:
            print("Sorry that's not enough money, Money refunded.")
            return False
        elif cost < paid:
            change = round((paid - cost), 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            return True


on = True
while on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == 'report':
        report_function()
    elif prompt == 'espresso':
        available = check_resources(prompt, water, milk, coffee)
        if available == 'True':
            price = money(prompt)
            if price:
                water -= 50
                coffee -= 18
                balance += 1.5
                print("Here is your espresso ☕ Enjoy!")
        else:
            print(f"Sorry there is not enough {available}.")
    elif prompt == 'latte':
        available = check_resources(prompt, water, milk, coffee)
        if available == 'True':
            price = money(prompt)
            if price:
                water -= 200
                milk -= 150
                coffee -= 24
                balance += 2.5
                print("Here is your latte ☕ Enjoy!")
        else:
            print(f"Sorry there is not enough {available}.")
    elif prompt == 'cappuccino':
        available = check_resources(prompt, water, milk, coffee)
        if available == 'True':
            price = money(prompt)
            if price:
                water -= 250
                milk -= 100
                coffee -= 24
                balance += 3.0
                print("Here is your cappuccino ☕ Enjoy!")
        else:
            print(f"Sorry there is not enough {available}.")
    elif prompt == 'off':
        on = False
