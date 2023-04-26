#!/usr/bin/env python3

decklist = input("Which decklist would you like to scan?: ")
card_dict = {}
banned = ["Bernard the Space Worm", "Cosmic Treasure", "Cosmic Treasure LOC", "Dark Space Eater", "Parallel Universe", "Slush Infestation", "shockwave 5"]
half_banned = ["Combine Harvester", "Pelfam", "Skeleghast", "Galaxy Crash", "Mystical Relic - Phantasmal Spoons", "For Sale Sign", "Phantom Matter", "Warphole Jetpack", "Beast of the Black Hole", "Planetary Field", "Pointurret", "Leviathan Crown"]

with open(decklist) as deck:
    cards = deck.readlines()
    for line in cards:
        new_line_index = line.index("\n")
        if line.startswith('//'):
            cards.remove(line)
        cardname = line[2:new_line_index]
        quantity = line[0]
        card_dict[cardname] = quantity

legality = 0
for card in card_dict:
    if int(card_dict[card]) > 2:
        legality -= 1
        print("You have "+card_dict[card]+"copies of "+card)
    elif card in banned:
        legality -= 1
        print(card+" is banned!")
    elif card in half_banned:
        if int(card_dict[card]) > 1:
            legality -= 1
            print(card+" is HALF-banned!")

if legality == 0:
    print("Deck is legal")
