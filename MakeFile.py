#!/usr/bin/env python3
import os

def test_fun(filename):
    with open(filename, "x") as f:
        print("The file known as {} has been born!".format(str(f)))

test_fun("/home/mikeyebert2004/testdir/testfile.txt")
