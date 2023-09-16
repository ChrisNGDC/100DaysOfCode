import art
from coffe_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine
from replit import clear

menu = Menu([
    MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
    MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
    MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
])
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

turn_off = False
print(art.title, art.logo)
while not turn_off:
    while True:
        user_drink = input('What would you like? (espresso/latte/cappuccino) → ').lower()
        if user_drink in ["off", "report"]:
            break
        user_drink = menu.find_drink(user_drink)
        if user_drink is not None:
            break
    if user_drink == 'off':
        turn_off = True
    elif user_drink == "report":
        clear()
        print(art.title, art.logo)
        coffe_maker.report()
        money_machine.report()
    else:
        if coffe_maker.is_resource_sufficient(user_drink):
            if money_machine.make_payment(user_drink.cost):
                coffe_maker.make_coffee(user_drink)
    clear()
    print(art.title, art.logo)
