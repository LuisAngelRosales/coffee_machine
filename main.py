from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
while True:
    choose=input(f"What drink do tou want? ({menu.get_items()}): ")
    if choose in ['espresso','latte','cappuccino']:
        order=menu.find_drink(choose)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
    elif choose == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choose=="off":
        break
    else:
        print("No valid option")

