#gamefunctions.py
#Breydon Wolff
#9/26/24

import random

def purchase_item(itemPrice: float, startingMoney: float, quantitytopurchase: int = 1):
    
    #Calculate cost for the requested ammount

    total_cost = itemPrice * quantitytopurchase
    
    #Figure out how many can be purchased

    if total_cost > startingMoney:
        quantity_purchased = int(startingMoney // itemPrice)
        leftover_money = startingMoney - (quantity_purchased * itemPrice)
    else:
        quantity_purchased = quantitytopurchase
        leftover_money = startingMoney - total_cost
    
    return quantity_purchased, leftover_money

def new_random_monster():
    monster_types = [
        {
            'name': 'Goblin',
            'description': 'A sneaky goblin lurks in the shadows, ready to pounce with a dagger.',
            'health': random.randint(20, 50),
            'power': random.randint(5, 15),
            'money': round(random.uniform(5, 20), 2)
        },
        {
            'name': 'Vulture',
            'description': 'A vulture circles overhead, eyeing potential prey with its sharp gaze.',
            'health': random.randint(1, 10),
            'power': random.randint(1, 5),
            'money': round(random.uniform(1, 10), 2)
        },
        {
            'name': 'Dragon',
            'description': 'A fearsome dragon breathes fire, guarding its treasure hoard.',
            'health': random.randint(100, 200),
            'power': random.randint(30, 50),
            'money': round(random.uniform(50, 100), 2)
        }
    ]
    
    # Randomly select a monster type

    selected_monster = random.choice(monster_types)
    return selected_monster

# new function known as print_welcome, which prints a welcome message

def print_welcome(name: str, width: int = 20):
    """Print a welcome message centered within a specified width."""
    message = f"Hello, {name}!"
    print(message.center(width))

# new function which outputs the shop menu

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """Print a shop menu listing two items with prices formatted."""
    border = "/" + "-" * 22 + "\\"
    item1_line = f"| {item1Name:<12}${item1Price:>6.2f} |"
    item2_line = f"| {item2Name:<12}${item2Price:>6.2f} |"
    print(border)
    print(item1_line)
    print(item2_line)
    print(border.replace("/", "\\").replace("\\", "/"))

# Demonstration of function calls

if __name__ == "__main__":

    # Purchase item(s) test
    num_purchased, leftover_money = purchase_item(1.5, 12, 4)
    print(f"Items Purchased: {num_purchased}, Money Remaining: {leftover_money}")

    num_purchased, leftover_money = purchase_item(1.44, 2.34, 5)
    print(f"Items Purchased: {num_purchased}, Money Remaining: {leftover_money}")

    num_purchased, leftover_money = purchase_item(4.23, 25.27)
    print(f"Items Purchased: {num_purchased}, Money Remaining: {leftover_money}")

    # new_random_monster test

    my_monster = new_random_monster()
    print(f"Monster: {my_monster['name']}")
    print(f"Description: {my_monster['description']}")
    print(f"Health: {my_monster['health']}, Money: {my_monster['money']}")

    my_monster = new_random_monster()
    print(f"Monster: {my_monster['name']}")
    print(f"Description: {my_monster['description']}")
    print(f"Health: {my_monster['health']}, Money: {my_monster['money']}")
    my_monster = new_random_monster()
    print(f"Monster: {my_monster['name']}")
    print(f"Description: {my_monster['description']}")
    print(f"Health: {my_monster['health']}, Money: {my_monster['money']}")

    #calling the new functions
    
    print_welcome("Jeff")
    print_welcome("Audrey")
    print_welcome("Maximiliano")

    print_shop_menu("Apple", 31, "Pear", 1.234)
    print_shop_menu("Egg", .23, "Bag of Oats", 12.34)
    print_shop_menu("Grapes", 2.5, "Chocolate Bar", 5.0)








