#!/usr/env/bin python3

decklist = input("Which decklist would you like to scan?: ")

with open(decklist) as deck:
   cards = deck.readlines()
   for line in cards:
       if line.startswith('//'):
           cards -= line
