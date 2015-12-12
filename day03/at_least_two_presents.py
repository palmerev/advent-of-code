#! /usr/bin/env python3

# the grid is a dictionary of coordinate tuples and integer present counts
# e.g. { (1,2): 1 }

from collections import defaultdict
from itertools import cycle
grid = defaultdict(int)
NORTH, SOUTH, EAST, WEST = '^', 'v', '>', '<'
# SANTA, ROBO = (0, 1)
santa_pos = [0, 0]
robo_pos = [0, 0]
santa_positions = cycle((santa_pos, robo_pos))
grid[tuple(santa_pos)] += 1
grid[tuple(robo_pos)] += 1

with open("input.txt", "r") as fin:
    for line in fin:
        line = line.strip()
        for direction in line:
            santa_position = next(santa_positions)
            if direction == NORTH:
                santa_position[1] += 1
            elif direction == SOUTH:
                santa_position[1] -= 1
            elif direction == EAST:
                santa_position[0] += 1
            elif direction == WEST:
                santa_position[0] -= 1
            grid[tuple(santa_position)] += 1

num_deliveries = len(grid)
print("num_deliveries:", num_deliveries)
