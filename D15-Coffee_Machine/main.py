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


money = 0


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
    missing_resources = []

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
    and handles the situation accordingly

    Args:
        coffee_type (String): Type of coffee (i.e. "espresso", "latte", or "cappuccino")
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
    print(sum)


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

    has_enough_resources = status["has_enough_resources"]

    if has_enough_resources:
        # process coins
        process_coins(coffee_type)
        return
    else:
        missing_resource = status["missing_resource"]
        print(f"Sorry there is not enough {missing_resource}.")


def coffee_machine():
    """
    Starts up the coffee machine software
    """
    is_on = True

    while (is_on):
        action = input(
            f"  What you would like? (espresso/latte/cappucino): ").lower()

        if action == "off":
            is_on = False
        elif action == "report":
            print_report()
        else:
            handle_coffee(action)

    return


coffee_machine()
