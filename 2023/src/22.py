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

#------------------------------------------------------------------------------
plano_z = {chave: [(x, y, b)    for b, brick in enumerate(bricks)
                                for x, y, z in brick if z == chave]
                                for chave in range(1, bricks[-1][-1][-1] + 1)}


#------------------------------------------------------------------------------
apoios = {chave: set() for chave in range(len(bricks))}
for i in range(len(bricks)-1, -1, -1):
    for x, y, z in bricks[i]:
        if d:=next((brick for brick in plano_z.get(z-1, [(-1,-1)])
                if (x, y) == brick[:2]), None):
            if d[2] == i:
                continue
            apoios[d[2]].add(i)

ans = 0
contado = set()
for b1, v1 in apoios.items():
    aux = set ()
    if not v1:
        ans += 1
        continue
    for b2, v2 in apoios.items():
        if b2 == b1 or not v2:
            continue 
        for val in v2:
            if val in v1:
                aux.add(val)
    if len(aux) == len(v1):
        ans += 1
print("--- Day 22: Sand Slabs ---")
print("Parte 1:", ans)

#70702
