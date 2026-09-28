"""
Program: Player class for the Match Coins Game (Lab 9)
Author: bjohnston14 (cet)
Purpose: Represent a player in the Match Coins game. A player has a name,
        a wallet of coins, and a Coin object to toss each round.
Starter code: None. Written from the Lab 9 assignment description.
Date: 2026-09-27
"""

from coin import Coin

class Player:

    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        self.__coin.toss()

    def get_coin_side(self):
        ret = self.__coin.get_sideup()
        return ret

    def win_coin(self):
        self.__wallet += 1

    def lose_coin(self):
        self.__wallet -= 1

    def get_wallet(self):
        ret = self.__wallet
        return ret

    def get_name(self):
        ret = self.__name
        return ret
