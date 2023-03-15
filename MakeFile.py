#!/usr/bin/env python3
import os
from pathlib import Path

def test_fun(filename):
    path = Path(filename)
    if path.is_file() == False:
        with open(filename, "x") as f:
            TextWrapper = str(f)
            cut_one = TextWrapper.index("name=")+5
            cut_two = TextWrapper.index(" mode=")
            MessagePiece = TextWrapper[cut_one:cut_two]
            print("The file known as {} has been born!".format(MessagePiece))
    else:
        print("File already exists")

f = input("What's the file's name?: ")
test_fun(f)
