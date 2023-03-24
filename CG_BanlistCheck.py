#!/usr/bin/env python3

decklist = input("Which decklist would you like to scan?: ")

with open(decklist) as deck:
    cards = deck.readlines()
    for line in cards:
        if line.startswith('//'):
            cards.remove(line)
    if 'deck-1' in cards:
        print("Non-card remover needs work")
    else:
        print("Non-card remover seems to work fine")
