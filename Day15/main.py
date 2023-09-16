import art
from replit import clear

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
units = ["ml", "ml", "g"]
money = 0


def report():
    i = 0
    for resource in resources:
        print(f'{resource.capitalize()}: {resources[resource]}{units[i]}')
        i += 1
    print(f'Money: ${money}')


def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            return ingredient
    return "None"


def check_out(drink, actual_money):
    drink_cost = MENU[drink]["cost"]
    print("Please insert some coins:\n")
    print(f"Latte cost → {drink_cost}")
    quarters = .25 * int(input("How many quarters? → "))
    dimes = .10 * int(input("How many dimes? → "))
    nickles = .05 * int(input("How many nickles? → "))
    pennies = .01 * int(input("How many pennies? → "))
    total = quarters + dimes + nickles + pennies
    if total > drink_cost:
        actual_money += drink_cost
        print(f'Here is ${total - drink_cost:.2f} dollars in change.')
        print(f'Here is your {drink} ☕ Enjoy it.')
    return actual_money


def make_drink(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]


turn_off = False
while not turn_off:
    clear()
    print(art.title, art.logo)
    user_drink = "None"
    while user_drink not in list(MENU.keys()) + ["off", "report"]:
        user_drink = input('What would you like? (espresso/latte/cappuccino) → ').lower()
    if user_drink == 'off':
        turn_off = True
    elif user_drink == "report":
        report()
    else:
        resource_needed = check_resources(user_drink)
        if resource_needed == "None":
            money_aux = check_out(user_drink, money)
            if money_aux != money:
                money = money_aux
                make_drink(user_drink)
            else:
                print(f"Sorry that's not enough money for a {user_drink}. Money refunded.")
        else:
            print(f'Not enough {resource_needed} for a {user_drink}')
