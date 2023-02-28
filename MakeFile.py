#!/usr/bin/env python3
import os

def test_fun(filename):
    with open(filename, "x") as f:
        print("The file known as {} has been born!".format(str(f)))

try:
    test_fun("~/home/mikeyebert2004/testdir/testfile.txt")
except:
    print(os.system('pwd'))
