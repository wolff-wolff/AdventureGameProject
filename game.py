#Game.py
#Breydon Wolff
#11-09-24

import json
import os
import random
from gamefunctions import print_welcome, new_random_monster


shop_items = [
    {"name": "sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10, "price": 50},
    {"name": "buckler", "type": "shield", "maxDurability": 6, "currentDurability": 6, "price": 30},
    {"name": "magic stone", "type": "consumable", "effect": "defeats one monster without loss of HP", "price": 20}
]

GRID_SIZE = 5  # Define grid size

class WanderingMonster:
    """Class to represent a wandering monster in the game."""

    def __init__(self, x: int, y: int, name: str, health: int, money: int):
        self.x = x  # Monster's x-coordinate
        self.y = y  # Monster's y-coordinate
        self.name = name
        self.health = health
        self.money = money

    def move(self):
        """Move the monster randomly within the grid bounds."""
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up' and self.y > 0:
            self.y -= 1
        elif direction == 'down' and self.y < GRID_SIZE - 1:
            self.y += 1
        elif direction == 'left' and self.x > 0:
            self.x -= 1
        elif direction == 'right' and self.x < GRID_SIZE - 1:
            self.x += 1

    def get_position(self):
        """Returns the current position of the monster."""
        return self.x, self.y

def save_game(filename: str, current_hp: int, current_gold: float, inventory: list) -> None:
    """Save the game state to a file in JSON format."""
    game_data = {
        'current_hp': current_hp,
        'current_gold': current_gold,
        'inventory': inventory
    }

    with open(filename, 'w') as file:
        json.dump(game_data, file)
    print(f"Game saved to {filename}.")

def load_game(filename: str) -> (int, float, list):
    """Load the game state from a file."""
    if not os.path.exists(filename):
        print("Save file does not exist. Starting new game.")
        return 30, 100, []  # Default starting values

    with open(filename, 'r') as file:
        game_data = json.load(file)

    current_hp = game_data.get('current_hp', 30)
    current_gold = game_data.get('current_gold', 100)
    inventory = game_data.get('inventory', [])

    print(f"Game loaded from {filename}.")
    return current_hp, current_gold, inventory

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
            choice = int(input("What would you like to do?\n1) Fight Monster\n2) Sleep (Restore HP for 5 Gold)\n3) Shop\n4) Equip Item\n5) Save and Quit\n6) Quit\n"))
            if choice in [1, 2, 3, 4, 5, 6]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
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

def encounter_with_monster(monster: WanderingMonster, current_hp: int, current_gold: float) -> (int, float):
    """Handle the encounter when the player and the monster are at the same location."""
    print(f"You encounter a {monster.name} at position ({monster.x}, {monster.y}) with {monster.health} HP!")

    while current_hp > 0 and monster.health > 0:
        damage_to_monster = random.randint(5, 10)
        damage_to_player = random.randint(3, 8)

        monster.health -= damage_to_monster
        current_hp -= damage_to_player

        print(f"You deal {damage_to_monster} damage to the {monster.name}.")
        print(f"The {monster.name} deals {damage_to_player} damage to you.")

    if monster.health <= 0:
        print(f"You defeated the {monster.name}!")
        current_gold += monster.money
    elif current_hp <= 0:
        print("You have been defeated.")

    return current_hp, current_gold

def move_player(player_x, player_y):
    """Prompt the player to move and update their position."""
    print(f"Your current position: ({player_x}, {player_y})")
    move = input("Which direction would you like to move? (up/down/left/right): ").lower()

    if move == "up" and player_y > 0:
        player_y -= 1
    elif move == "down" and player_y < GRID_SIZE - 1:
        player_y += 1
    elif move == "left" and player_x > 0:
        player_x -= 1
    elif move == "right" and player_x < GRID_SIZE - 1:
        player_x += 1
    else:
        print("Invalid move or you've hit the boundary.")

    return player_x, player_y
def main():
    print("Welcome to the Adventure Game!")

    # Loop until the user enters a valid choice (1 or 2)
    while True:
        choice = input("Do you want to (1) Start a new game or (2) Load a saved game? ")

        if choice == '1':
            player_name = input("Enter your name: ")
            print_welcome(player_name)
            current_hp = 30  # Starting HP
            current_gold = 100  # Starting Gold
            inventory = []  # Start with an empty inventory
            player_x, player_y = 2, 2  # Start player at center of grid
            monsters = [WanderingMonster(random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1), "Goblin", 20, 10)]  # Initialize monsters
            break  # Exit the loop to proceed with the game

        elif choice == '2':
            filename = input("Enter the save file name to load: ")
            current_hp, current_gold, inventory = load_game(filename)
            player_x, player_y = 2, 2  # Start player at center of grid if loaded
            monsters = [WanderingMonster(random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1), "Goblin", 20, 10)]  # Initialize monsters
            break  # Exit the loop to proceed with the game

        else:
            print("Invalid choice. Please enter '1' to start a new game or '2' to load a saved game.")

    # Main game loop
    while True:
        display_status(current_hp, current_gold, inventory)

        # Call the move_player function each turn to move the player
        player_x, player_y = move_player(player_x, player_y)

        choice = get_user_choice()

        if choice == 1:
            # Check if player is at the same position as any monster
            for monster in monsters:
                if (player_x, player_y) == monster.get_position():
                    current_hp, current_gold = encounter_with_monster(monster, current_hp, current_gold)
                    if current_hp <= 0:
                        print("You have been defeated.")
                        return
                    break

        elif choice == 2:
            current_hp, current_gold = sleep(current_hp, current_gold)
        elif choice == 3:
            current_gold = shop(current_gold, inventory)  # Call the shop function
        elif choice == 4:
            equip_item(inventory)  # Equip an item
        elif choice == 5:
            filename = input("Enter filename to save your game: ")
            save_game(filename, current_hp, current_gold, inventory)
            break
        elif choice == 6:
            print("Thanks for playing!")
            break

        # Move monsters
        for monster in monsters:
            monster.move()

        # Check if player encounters any monster
        for monster in monsters:
            if (player_x, player_y) == monster.get_position():
                current_hp, current_gold = encounter_with_monster(monster, current_hp, current_gold)
                if current_hp <= 0:
                    print("You have been defeated.")
                    return

        # If all monsters are defeated, spawn new monsters
        if all(monster.health <= 0 for monster in monsters):
            print("All monsters defeated! New monsters are appearing!")
            monsters = [
                WanderingMonster(random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1), "Goblin", 20, 10),
                WanderingMonster(random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1), "Orc", 25, 15)
            ]

if __name__ == "__main__":
    main()  # This runs the main game function
