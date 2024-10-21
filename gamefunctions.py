#gamefunctions.py
#Breydon Wolff
#9/26/24

"""
Game Functions Module

This module provides functions for a simple computer game. It includes
functionality for greeting players, displaying a shop menu, purchasing
items, generating random monsters, and displaying a shop menu.

Functions:
- print_welcome: Prints a welcome message to the player.
- print_shop_menu: Displays a menu with items and their prices.
- purchase_item: Handles the purchasing logic for items.
- new_random_monster: Generates and returns a random monster.

Typical usage example:

    from gamefunctions import print_welcome
    print_welcome("Player Name")
"""
import random

def purchase_item(itemPrice: float, startingMoney: float, quantitytopurchase: int = 1) -> tuple:
    """
    Handle the purchasing logic for items.

    Parameters:
        itemPrice (float): Price of a single item.
        startingMoney (float): Amount of money the player has.
        quantitytopurchase (int): Number of items to purchase (default is 1).

    Returns:
        tuple: A tuple containing the number of items purchased and the 
               leftover money.

    Example:
        >>> purchase_item(2.5, 10, 3)
        (4, 0.0)
    """
    # Calculate cost for the requested amount
    total_cost = itemPrice * quantitytopurchase

    # Figure out how many can be purchased
    if total_cost > startingMoney:
        quantity_purchased = int(startingMoney // itemPrice)
        leftover_money = startingMoney - (quantity_purchased * itemPrice)
    else:
        quantity_purchased = quantitytopurchase
        leftover_money = startingMoney - total_cost

    return quantity_purchased, leftover_money

def new_random_monster() -> dict:
    """
    Generate and return a random monster.

    Returns:
        dict: A dictionary containing the monster's name, description, 
              health, power, and money.

    Example:
        >>> monster = new_random_monster()
        >>> monster['name']
        'Goblin'  # This will vary as it is random
    """
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

    """
    Print a welcome message centered within a specified width.

    Parameters:
        name (str): The name of the player.
        width (int): The width for centering the message (default is 20).

    Returns:
        None

    Example:
        >>> print_welcome("Jeff")
        '      Hello, Jeff!      '
    """
    
    message = f"Hello, {name}!"
    print(message.center(width))

# new function which outputs the shop menu

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
    """
    Print a shop menu listing two items with prices formatted.

    Parameters:
        item1Name (str): Name of the first item.
        item1Price (float): Price of the first item.
        item2Name (str): Name of the second item.
        item2Price (float): Price of the second item.

    Returns:
        None

    Example:
        >>> print_shop_menu("Apple", 1.5, "Pear", 2.0)
    """
    border = "/" + "-" * 22 + "\\"
    item1_line = f"| {item1Name:<12}${item1Price:>6.2f} |"
    item2_line = f"| {item2Name:<12}${item2Price:>6.2f} |"
    print(border)
    print(item1_line)
    print(item2_line)
    print(border.replace("/", "\\").replace("\\", "/"))

# New function that demonstrates the use of the functions

def test_functions():
    """Run tests on the module's functions."""
    # Test purchase_item
    num_purchased, leftover_money = purchase_item(1.5, 12, 4)
    print(f"Items Purchased: {num_purchased}, Money Remaining: {leftover_money}")

    # Test new_random_monster
    for _ in range(3):
        my_monster = new_random_monster()
        print(f"Monster: {my_monster['name']}, Health: {my_monster['health']}")

    # Test print_welcome
    print_welcome("Jeff")
    
    # Test print_shop_menu
    print_shop_menu("Apple", 1.5, "Pear", 2.0)

if __name__ == "__main__":
    test_functions()









