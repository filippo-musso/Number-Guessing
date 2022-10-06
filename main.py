#!/usr/bin/env python

# A very simple game created in a dead time, that makes you guess a numbers randomly picked by the program

import __generate
import __tips
import __prize

print('Benvenuti nel gioco "indovina il numero"... partiamo!!!')

print('\n\nGenerando il numero...\n\n')

number = __generate.number()

guessed = False
tries = 0

while True:
    guess = int(input("Prova a indovinarlo: "))
    if guess != number:
        __tips.giver(number, guess)
        tries = int(__prize.calculator(tries, guessed))
    else:
        guessed = True
        print(__prize.calculator(tries, guessed))
        break

__author__ = "Filippo Musso"
__copyright__ = "Copyright 2022, The Cogent Project"
__credits__ = "Filippo Musso"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Filippo Musso"
__email__ = "fili.musso05@gmail.com"
__status__ = "Prototype"
