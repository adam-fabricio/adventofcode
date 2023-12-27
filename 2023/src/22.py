#!/usr/bin/env python3


import os
import re
from sys import argv


test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]

if test:
    dia = dia + "_test"
path = os.path.join("data", dia)
with open(path) as f:
    arquivo = f.read().splitlines()
#---------------------------------parsing-------------------------------------
bricks = sorted([[(x, y, z)
                  for x in range(min(b1[0], b2[0]), max(b1[0], b2[0])+1)
                  for y in range(min(b1[1], b2[1]), max(b1[1], b2[1])+1)
                  for z in range(min(b1[2], b2[2]), max(b1[2], b2[2])+1)]
                 for (b1, b2) in ([tuple(map(int, cordenadas.split(',')))
                                   for cordenadas in linha.split("~")]
                                  for linha in arquivo)],
                key=lambda x: x[-1][-1], reverse=False)
#---------------------------------assentamento---------------------------------
altura = {}
for cs, cubes in enumerate(bricks):
    flag = 0
    d_z = 10000
    for cube in cubes:
        x, y, z = cube
        d_z = min(z - (altura.get((x, y), 0) + 1), d_z)
    for c, cube in enumerate(cubes):
        x, y, z = cube
        bricks[cs][c] = (x, y, z-d_z)
        altura[(x, y)] = z-d_z
print(len(bricks))
#------------------------------------------------------------------------------


