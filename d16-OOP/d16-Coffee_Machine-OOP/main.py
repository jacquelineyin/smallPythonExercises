from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()


def print_reports():
    coffeeMaker.report()
    moneyMachine.report()


def handle_transaction(drink_name):
    drink = menu.find_drink(drink_name)

    if not coffeeMaker.is_resource_sufficient(drink):
        print(f"Sorry, there are not enough ingredients to make {drink}.")
    else:
        was_successful = moneyMachine.make_payment(drink.cost)
        if not was_successful:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            coffeeMaker.make_coffee(drink)


def coffee_machine():
    is_on = True
    menu_items = menu.get_items()

    while is_on:
        user_choice = input(
            f"What would you like? ({menu_items.rstrip(menu_items[-1])}): ").lower()

        if user_choice == "off":
            is_on = False
        elif user_choice == "report":
            print_reports()
        elif user_choice in menu.get_items().split("/"):
            handle_transaction(user_choice)
        else:
            print(f"Invalid input. Please try again.")

    return


coffee_machine()
