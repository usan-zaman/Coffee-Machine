MENU = {
    "espresso": {
        "ingredients": {
            "water": 52,
            "coffee": 17,
        },
        "cost": 1.6,
    },
    "latte": {
        "ingredients": {
            "water": 205,
            "milk": 156,
            "coffee": 23,
        },
        "cost": 2.7,
    },
    "cappuccino": {
        "ingredients": {
            "water": 240,
            "milk": 100,
            "coffee": 25 ,
        },
        "cost": 3.5,
    }
}
profit= 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f" Sorry ,there is not enough {item} ")
            return False
    return is_enough

def process_coins():
    print("Please insert coins.")
    total= int(input("How many quarters: ")) * 0.25
    total += int(input("How many dines: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennis: ")) * 0.01
    return total

def is_transaction_success (money_received , drink_cost):
    if money_received >= drink_cost:
        change= round(money_received-drink_cost,2 )
        print(f"Here is ${change} for change.")
        global profit
        profit+= drink_cost
        return True
    else:
        print("Sorry, You have not sufficienr money.")

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    print(f"This is your {drink_name}")

is_one= True

while is_one:
    choice= input("What would you like to choice? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_one= False
    elif choice== "report":
        print(f"water:{resources['water']} ml")
        print(f"milk: {resources['milk' ]} ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment= process_coins()
            if is_transaction_success(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])





