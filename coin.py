"""
Program: Coin class for the Match Coins Game (Lab 9)
Author: bjohnston14 (cet)
Purpose: Represent a single tossable coin. The coin only knows its own
        state: which side is currently facing up ('Heads' or 'Tails').
Starter code: None. Written from the Lab 9 assignment description.
Date: 2026-09-27
"""

import random

class Coin:

    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        ret = self.__sideup
        return ret
