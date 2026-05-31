from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine=MoneyMachine()
resources=CoffeeMaker()
my_money_machine.report()
resources.report()
menu=Menu()
is_on=True
while is_on:
    options=menu.get_items()
    choice=input(f"what would you like to drink(latte/espresso/cappuccino){options}")
    if choice=="off":
        is_on=False
    elif choice=="report":
        my_money_machine.report()
        resources.report()
    else:
        drink=menu.find_drink(choice)
        if resources.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
             resources.make_coffee(drink)


