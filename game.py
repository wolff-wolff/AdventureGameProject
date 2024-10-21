#Game.py
#Breydon Wolff
#10-16-24

from gamefunctions import print_welcome, print_shop_menu, purchase_item, new_random_monster

def main():
    """Main function to run the game."""
    player_name = input("Enter your name: ")
    print_welcome(player_name)

    print("Welcome to the shop!")
    print_shop_menu("Apple", 1.5, "Pear", 2.0)
    
    item_price = float(input("Enter the price of the item you want to buy: "))
    starting_money = float(input("Enter your starting money: "))
    quantity = int(input("Enter quantity to purchase: "))
    
    num_purchased, leftover_money = purchase_item(item_price, starting_money, quantity)
    print(f"Items Purchased: {num_purchased}, Money Remaining: {leftover_money}")

    monster = new_random_monster()
    print(f"You encounter a {monster['name']}!")
    print(f"Description: {monster['description']}")
    print(f"Health: {monster['health']}, Money: {monster['money']}")

if __name__ == "__main__":
    main()
