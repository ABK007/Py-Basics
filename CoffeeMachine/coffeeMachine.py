
# Contains the ingredients amount for each type of coffee and its cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
# Resources available to machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
# contains the value of each type of coin
coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25
}


def print_report(money):
    """Displays the available resources report"""

    report = (f" Water: {resources['water']}ml \n Milk: {resources['milk']}ml \n Coffee: {resources['coffee']}g \n Money: ${money}")
    return report


def coffee_ingredients(coffee_type):
    """Evaluates the amount of ingredients based on type of coffee"""

    coffee_type = MENU[coffee_type]
    ingredients = coffee_type['ingredients']
    water_qty = ingredients['water']
    coffee_qty = ingredients['coffee']
    milk_qty = ingredients['milk']


    water_resource = resources['water']
    coffee_resource = resources['coffee']
    milk_resource = resources['milk']


    remaining_water = water_resource - water_qty
    remaining_coffee = coffee_resource - coffee_qty
    remaining_milk =  milk_resource - milk_qty

    resources['water'] = remaining_water
    resources['coffee'] = remaining_coffee
    resources['milk'] = remaining_milk

    if remaining_water < 0:
        return 1

    elif remaining_coffee < 0:
        return 2

    elif remaining_milk < 0:
        return 3
    else:
        return 4



def process_coins(coffee_cost,quater_count, dime_count, nickel_count, penny_count):
    """returns the change by calculating the coins"""
    total_amount = (quater_count * coins['quarter'] + \
                    dime_count * coins['dime'] + \
                    nickel_count * coins['nickel'] + \
                    penny_count * coins['penny'])

    if total_amount >= coffee_cost:
        return total_amount - coffee_cost
    else:
        return 0


def processing_payment(coffee_type):
    """returns the cost of coffee based on type of coffee"""
    return MENU[coffee_type]['cost']


def coffee_machine():
    """Contains the main code of coffee machine"""

    money = 0 # initial profit

    while True:

        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input == "report":
            print(print_report(money))

        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            print("please insert coins!")
            # Asks to enter coins
            quater_count = int(input("how many quarters? "))
            dime_count = int(input("how many dimes? "))
            nickel_count = int(input("how many nickels? "))
            penny_count = int(input("how many pennies? "))

            cost = processing_payment(user_input) # saves the cost of coffee typed by the user
            # The change left after paying the amount of coffee
            change = round(process_coins(cost, quater_count, dime_count, nickel_count, penny_count), 2)

            if change == 0:
                print("Sorry! that's not enough money. money refunded")
            else:
                ingredients = (coffee_ingredients(user_input))

                if ingredients == 4:
                    print("Here is your coffee, ☕")
                    print(f"here is your change ${change}")
                    money += cost

                elif ingredients == 3:
                    print("Sorry Not enough milk is available")

                elif ingredients == 2:
                    print("Sorry Not enough coffee is available")
                else:
                    print("Sorry Not enough water is available")


        elif user_input == "exit":
            print("Have a great day, bye bye")
            break

        else:
            print("please enter correct coffee name")




coffee_machine()









