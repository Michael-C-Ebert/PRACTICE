#!/usr/bin/env python3

CST_hour = int(input("Enter the CST hour here: "))
CST_minutes = int(input("Enter the CST minutes here: "))
timezones = ["CST", "CET", "BST", "UTC+3"]
time_stamps = {"timezone":"time"}
minutes = ":" + str(CST_minutes)

CST_time = str(CST_hour) + minutes
time_stamps["CST time"] = CST_time

CET_time = str(CST_hour+7) + minutes
time_stamps["CET time"] = CET_time

BST_time = str(CST_hour+6) + minutes
time_stamps["BST time"] = BST_time

UTC3_time = str(CST_hour+8) + minutes
time_stamps["UTC+3 time"] = UTC3_time

for item in time_stamps:
    print(item)
