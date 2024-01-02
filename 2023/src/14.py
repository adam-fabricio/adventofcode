#!/usr/bin/env python3


import os
import re
from sys import argv
from functools import cache


def calc( m_l, r ):
    ans = 0
    for rock_x, rock_y in r:
        ans += m_l - rock_x
    return ans


def print_map(m_l, m_c, r, w ):
    for l in range(m_l):
        for c in range(m_c):
            if (l, c) in w:
                print("#", end='')
            elif [l, c] in r:
                print("O", end='')
            else:
                print(".", end='')
        print()
    print("=" * 80)


def move( direction: str, rocks: list, wall:set ) -> list:
    if direction == "up":
        d = (-1, 0)
        rocks.sort(key = lambda x: x[0] )
    elif direction == "left":
        rocks.sort(key = lambda x: x[1] )
        d = (0, -1)
    elif direction == "down":
        rocks.sort(reverse = True, key = lambda x: x[0] )
        d = (1, 0)
    elif direction == "right":
        d = (0, 1)
        rocks.sort(reverse = True, key = lambda x: x[1] )


    new_rocks = []

    for rock in rocks:
        while True:
            new_rock_l = rock[0] + d[0]
            new_rock_c = rock[1] + d[1]
            new_rock = (new_rock_l, new_rock_c)
            if ( new_rock_l < 0 or new_rock_c < 0
                    or new_rock_l >= max_lines or new_rock_c >= max_col
                    or new_rock in wall or list(new_rock) in new_rocks ):
                new_rocks.append ( rock )
                break
            else:
                rock = list(new_rock)
    return new_rocks


test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]
dia = dia + "_test" if test else dia
path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()


max_lines = len(arquivo)
max_col = len(arquivo[0])

wall = { (l, c) for l, line in enumerate(arquivo)
        for c, char in enumerate(line) if char == "#" }

rocks = sorted([ [l, c] for l, line in enumerate(arquivo)
    for c, char in enumerate(line) if char == "O" ], key=lambda x: x[0] )

ans = move("up", rocks, wall)
#print(ans)

cicle = ["up", "left", "down", "right"]

rep = 0
ans = []
set_rocks = set()
for i in range(160):
    for direction in cicle:
        rocks = move(direction, rocks, wall)
    print(i)

    #val = calc(max_lines, rocks)
    #rock = tuple(map(tuple, rocks))
    #if (rock, val) in set_rocks:
    #    ans.append( (i, val) )
    #    set_rocks = set()
    #    if rep == 2:
    #        break
    #    rep += 1
    #set_rocks.add((rock, val))

print(calc(max_lines, rocks))

# [(9, 69), (16, 69), (23, 69)]
# [(152, 104667), (166, 104667), (180, 104667)]


