#!/usr/bin/env python3
import os

def test_fun(filename):
    with open(filename, "x") as f:
        print("The file known as {} has been born!".format(str(f)))

os.system('cd ..')
try:
    test_fun("testdir/testfile.txt")
except:
    print(os.system('pwd'))

