#Game.py
#Breydon Wolff
#10-16-24

from gamefunctions import print_welcome, new_random_monster
import random


shop_items = [
    {"name": "sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10, "price": 50},
    {"name": "buckler", "type": "shield", "maxDurability": 6, "currentDurability": 6, "price": 30},
    {"name": "magic stone", "type": "consumable", "effect": "defeats one monster without loss of HP", "price": 20}
]


def shop(current_gold: float, inventory: list) -> float:
    """Display shop items and allow the player to purchase them."""
    print("Welcome to the shop! You have", current_gold, "gold.")
    print("Items available for purchase:")

    for index, item in enumerate(shop_items):
        print(f"{index + 1}) {item['name']} - Price: {item['price']} Gold")

    choice = input("Enter the number of the item you want to buy (or 'none' to exit): ")

    if choice.isdigit() and 1 <= int(choice) <= len(shop_items):
        item_to_buy = shop_items[int(choice) - 1]

        if current_gold >= item_to_buy['price']:
            current_gold -= item_to_buy['price']
            inventory.append(item_to_buy)
            print(f"You bought a {item_to_buy['name']}!")
        else:
            print("Not enough gold to buy this item.")
    elif choice.lower() == 'none':
        print("Leaving the shop.")
    else:
        print("Invalid choice.")

    return current_gold


def equip_item(inventory: list) -> None:
    """Allow the player to equip an item from their inventory."""
    weapon_choices = [item for item in inventory if item['type'] == 'weapon']

    if not weapon_choices:
        print("You have no weapons to equip.")
        return

    print("Choose a weapon to equip:")
    for index, item in enumerate(weapon_choices):
        print(f"{index + 1}) {item['name']} (Durability: {item['currentDurability']}/{item['maxDurability']})")

    choice = input("Enter the number of the item to equip, or 'none' to cancel: ")
    if choice.isdigit() and 1 <= int(choice) <= len(weapon_choices):
        equipped_item = weapon_choices[int(choice) - 1]
        print(f"You have equipped the {equipped_item['name']}!")
    elif choice.lower() == 'none':
        print("No item equipped.")
    else:
        print("Invalid choice.")



def display_status(current_hp: int, current_gold: float, inventory: list) -> None:
    """Display current HP, Gold, and Inventory."""
    print(f"Current HP: {current_hp}, Current Gold: {current_gold}")
    print("Inventory:")
    for item in inventory:
        print(f"- {item['name']} (Type: {item['type']})")
    print()

def get_user_choice() -> int:
    """Get a valid choice from the user."""
    while True:
        try:
            choice = int(input("What would you like to do?\n1) Fight Monster\n2) Sleep (Restore HP for 5 Gold)\n3) Shop\n4) Equip Item\n5) Quit\n"))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")


def fight_monster(current_hp: int, current_gold: float, inventory: list) -> (int, float):
    """Handle fighting a monster."""
    monster = new_random_monster()
    monster_health = monster['health']

    print(f"You encounter a {monster['name']}! Health: {monster_health}")

    while current_hp > 0 and monster_health > 0:
        damage_to_monster = random.randint(5, 10)
        damage_to_player = random.randint(3, 8)

        monster_health -= damage_to_monster
        current_hp -= damage_to_player

        print(f"You deal {damage_to_monster} damage to the {monster['name']}.")
        print(f"The {monster['name']} deals {damage_to_player} damage to you.")

    if monster_health <= 0:
        print(f"You defeated the {monster['name']}!")
        current_gold += monster['money']
    elif current_hp <= 0:
        print("You have been defeated.")

    return current_hp, current_gold

def sleep(current_hp: int, current_gold: float) -> (int, float):
    """Restore HP by sleeping."""
    if current_gold >= 5:
        current_gold -= 5
        current_hp += 10  # Restore 10 HP
        print("You rest and recover 10 HP.")
    else:
        print("Not enough gold to sleep.")
    return current_hp, current_gold

def main():
    """Main function to run the game."""
    player_name = input("Enter your name: ")
    print_welcome(player_name)

    current_hp = 30  # Starting HP
    current_gold = 100  # Starting Gold
    inventory = []  # Start with an empty inventory

    while True:
        display_status(current_hp, current_gold, inventory)
        choice = get_user_choice()

        if choice == 1:
            current_hp, current_gold = fight_monster(current_hp, current_gold, inventory)
        elif choice == 2:
            current_hp, current_gold = sleep(current_hp, current_gold)
        elif choice == 3:
            current_gold = shop(current_gold, inventory)  # Call the shop function
        elif choice == 4:
            equip_item(inventory)  # Equip an item
        elif choice == 5:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
