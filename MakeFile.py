#!/usr/bin/env python3
import os

def test_fun(filename):
    with open(filename, "x") as f:
        TextWrapper = str(f)
        cut_one = TextWrapper.index("name=")
        cut_two = TextWrapper.index(" mode=")
        MessagePiece = TextWrapper[cut_one:cut_two]
        print("The file known as {} has been born!".format(MessagePiece))

test_fun("/home/mikeyebert2004/testdir/testfile.txt")
