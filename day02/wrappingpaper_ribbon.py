#! /usr/bin/env python3

total_paper_feet = 0
total_ribbon_feet = 0
with open("input.txt", "r") as fin:
    for line in fin:
        present = line.strip()
        length, width, height = [int(x) for x in present.split('x')]
        dims = sorted([length, width, height])
        # get the two smallest dimensions for ribbon calculation
        smallest_dims = dims[:2]
        present_ribbon = 2 * (smallest_dims[0] + smallest_dims[1])
        bow_ribbon = length * width * height
        total_ribbon_feet += present_ribbon + bow_ribbon

        side1 = 2 * length * width
        side2 = 2 * width * height
        side3 = 2 * length * height
        small_side = min(side1, side2, side3) / 2

        total_paper_feet += sum([side1, side2, side3, small_side])
    print("total paper feet: ", total_paper_feet)
    print("total ribbon feet: ", total_ribbon_feet)
