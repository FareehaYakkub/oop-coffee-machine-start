from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()


is_on = True
moneymachine = MoneyMachine()

while is_on:
    options = menu.get_items()
    print(options)
    choice = input(f"What would you like? ({options})")

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


