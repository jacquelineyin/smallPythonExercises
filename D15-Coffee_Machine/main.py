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


money = 0.00


def print_report():
    """
    Prints the amount of resources and money left in the machine
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def check_resources(coffee_type):
    """Checks to see if machine's resources are sufficient to make given type of coffee

    Args:
        coffee_type (String): Type of coffee (i.e. "espresso", "latte", or "cappuccino")

    Returns:
        Object: {"has_enough_resources": boolean, "missing_resource": String or None} 
    """
    needed_ingredients = MENU[coffee_type]["ingredients"]
    has_enough_resources = True

    for resource in needed_ingredients:
        if resources[resource] < needed_ingredients[resource]:
            return {"has_enough_resources": False, "missing_resource": resource}

    return {"has_enough_resources": has_enough_resources, "missing_resource": None}


def calculate_amount(money):
    """Takes a dictionary of coins, and calculates the total sum

    Args:
        money (Dictionary): A dictionary object of coins with the values being the number of coin type

    Returns:
        float: total sum of the coin values, rounded to 2 decimal places
    """
    quarters_sum = money["quarters"] * 0.25
    dimes_sum = money["dimes"] * 0.1
    nickles_sum = money["nickles"] * 0.05
    pennies_sum = money["pennies"] * 0.01

    total = quarters_sum + dimes_sum + nickles_sum + pennies_sum
    return round(total, 2)


def process_coins(coffee_type):
    """
    Intakes user's coins and checks to see if amount is sufficient

    Args:
        coffee_type (String): Type of coffee (i.e. "espresso", "latte", or "cappuccino")

    Returns:
        boolean: True if user gives sufficient amount of money for given coffee_type
    """
    print("Please insert coins.")

    MONEY = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0,
    }

    for coin in MONEY:
        MONEY[coin] = int(input(f"How many {coin}?: "))

    sum = calculate_amount(MONEY)
    return {"is_sufficient": sum >= MENU[coffee_type]["cost"], "total": sum}


def handle_change(coffee_type, money_received):
    """If we receive more money than the coffee_type costs, returns the change to the user

    Args:
        coffee_type (String): Type of coffee (i.e. "espresso", "latte", or "cappuccino")
        money_received (float): Money received from user
    """
    cost = MENU[coffee_type]["cost"]

    if money_received > cost:
        change = round(money_received - cost, 2)
        print(f"Here is ${change:.2f} dollars in change.")


def complete_transaction(coffee_type, money_received):
    """
    Deducts ingredients of coffee_type from machine's resources,
    Gives user change for money_received as appropriate to the situation
    Updates the money in the machine
    And gives the completed drink back to the user

    Args:
        coffee_type ([type]): [description]
        money_received ([type]): [description]
    """
    global money

    coffee_ingredients = MENU[coffee_type]["ingredients"]

    for ingredient in coffee_ingredients:
        resources[ingredient] -= coffee_ingredients[ingredient]

    money = round(money + MENU[coffee_type]["cost"], 2)
    handle_change(coffee_type, money_received)

    print(f"Here is your {coffee_type}. Enjoy!")


def handle_coffee(coffee_type):
    """
    Checks if there are sufficient resources for given coffee type.
    If there resources are sufficient, payment is processed
    Otherwise, an error message is given as feedback to user.

    Args:
        coffee_type (String): Type of coffee (i.e. "espresso", "latte", or "cappuccino")
    """
    has_enough_resources = None

    if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        status = check_resources(coffee_type)
    else:
        print("Invalid command. Please try again.")
        return

    has_enough_resources = status["has_enough_resources"]

    if has_enough_resources:
        handle_transaction(coffee_type)
    else:
        missing_resource = status["missing_resource"]
        print(f"Sorry, there is not enough {missing_resource}.")


def handle_transaction(coffee_type):
    """
    Takes coffee_type and gets payment from users. 
    Handles transaction depending on whether payment is sufficient or not

    Args:
        coffee_type (String): Type of coffee (i.e. "espresso", "latte", or "cappuccino")
    """
    coins_received_info = process_coins(coffee_type)
    is_sufficient = coins_received_info["is_sufficient"]

    if (is_sufficient):
        complete_transaction(coffee_type, coins_received_info["total"])
    else:
        print("Sorry, that's not enough money. Money refunded.")


def coffee_machine():
    """
    Starts up the coffee machine software
    """
    is_on = True

    while (is_on):
        action = input(
            f"  What you would like? (espresso/latte/cappuccino): ").lower()

        if action == "off":
            is_on = False
        elif action == "report":
            print_report()
        else:
            handle_coffee(action)


# Start Program
coffee_machine()
