#!/usr/bin/env python3

STR = input("Please give a word, phrase, or sentence: ")

unallowed = "' ?/![]{}()*&^%$#@=+-_;:.,/" + '"'
counter = 0

for char in STR:
    if char in unallowed:
        counter += 1

print(len(STR)-counter)
