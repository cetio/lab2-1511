"""
Program: Match Coins Game (Lab 9)
Author: bjohnston14 (cet)
Purpose: Run an interactive coin-tossing game between two players. Each
        round both players toss their coin; if the sides match Player 1
        wins a coin, otherwise Player 2 wins a coin. The game ends when
        the user quits or a player's wallet reaches 0.
Starter code: None. Written from the Lab 9 assignment description.
        Uses coin.py and player.py from this lab.
Date: 2026-09-27
"""

from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
    print()

    choice = input("Do you want to toss the coins? (y/n): ")
    print()

    while choice == 'y' or choice == 'Y':
        player1.toss_coin()
        player2.toss_coin()
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print("Tossing...")
        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"...It's a Match! {player1.get_name()} wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print(f"...No Match! {player2.get_name()} wins a coin.")

        print()
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
        print()

        if player1.get_wallet() == 0 or player2.get_wallet() == 0:
            print("--- Game Over ---")
            print("A player's wallet is empty!")
            print()
            break

        choice = input("Do you want to toss the coins? (y/n): ")
        print()

    print("--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins with more coins!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins with more coins!")
    else:
        print("It's a draw!")

main()
