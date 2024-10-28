#Game.py
#Breydon Wolff
#10-16-24

from gamefunctions import print_welcome, new_random_monster
import random

def display_status(current_hp: int, current_gold: float) -> None:
    """Display current HP and Gold."""
    print(f"Current HP: {current_hp}, Current Gold: {current_gold}")

def get_user_choice() -> int:
    """Get a valid choice from the user."""
    while True:
        try:
            choice = int(input("What would you like to do?\n1) Fight Monster\n2) Sleep (Restore HP for 5 Gold)\n3) Quit\n"))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def fight_monster(current_hp: int, current_gold: float) -> (int, float):
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
    current_gold = 10  # Starting Gold

    while True:
        display_status(current_hp, current_gold)
        choice = get_user_choice()

        if choice == 1:
            current_hp, current_gold = fight_monster(current_hp, current_gold)
        elif choice == 2:
            current_hp, current_gold = sleep(current_hp, current_gold)
        elif choice == 3:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
