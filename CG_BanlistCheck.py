#!/usr/bin/env python3

decklist = input("Which decklist would you like to scan?: ")
card_dict = {}

with open(decklist) as deck:
    cards = deck.readlines()
    for line in cards:
        new_line_index = line.index("\n")
        if line.startswith('//'):
            cards.remove(line)
        cardname = line[2:new_line_index]
        quantity = line[0]
        card_dict[cardname] = quantity

print(card_dict)
