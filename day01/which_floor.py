#! /usr/bin/env python3
from sys import exit
floor = 0
position = 0
with open("input.txt") as fin:
    for line in fin:
        for char in line:
            position += 1
            print("floor: ", floor)
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1
            else:
                break
            if floor == -1:
                print("position: ", position)
                break
