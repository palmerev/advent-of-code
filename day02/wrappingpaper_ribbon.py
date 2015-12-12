#! /usr/bin/env python3

total_feet = 0
with open("input.txt", "r") as fin:
    for line in fin:
        present = line.strip()
        length, width, height = [int(x) for x in present.split('x')]

        side1 = 2 * length * width
        side2 = 2 * width * height
        side3 = 2 * length * height
        small_side = min(side1, side2, side3) / 2
        total_feet += sum([side1, side2, side3, small_side])
    print("total feet: ", total_feet)
