#!/usr/bin/env python3


import os
import re
import sys
import subprocess

test = 0
part = "1"
dia = "10"

sys.setrecursionlimit(10**6)

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

mapa = {}
for l, lines in enumerate(arquivo):
    for c, col in enumerate(lines):
        if col == ".":
            continue
        mapa[(l, c)] = []
        if col == "S":
            start = (l, c)
            direcoes = [ (0,1), (1,0), (0,-1), (-1,0) ]
        elif col == "-":
            direcoes = [ (0,1), (0,-1) ]
        elif col == "|":
            direcoes = [(-1,0), (1,0) ]
        elif col == "L":
            direcoes = [ (-1,0 ), (0, 1) ]
        elif col == "J":
            direcoes = [ (-1, 0), (0, -1) ]
        elif col == "7":
            direcoes = [ (0, -1), (1, 0) ]
        elif col == "F":
            direcoes = [ (1, 0), (0, 1) ]

        for i, j in direcoes:
            if i+l < 0 or i+l >= len(arquivo) or j+c < 0 or j+c >= len(lines):
                continue
            elif arquivo[i+l][j+c] == ".":
                continue
            elif i == -1 and arquivo[i+l][j+c] in "-JL":
                continue
            elif i == 1 and arquivo[i+l][j+c] in "-F7":
                continue
            elif j == -1 and arquivo[i+l][j+c] in "|J7":
                continue
            elif j == 1 and arquivo[i+l][j+c] in "|FL":
                #print(l,c, arquivo[i+l][j+c])
                continue
            mapa[(l, c)].append( (i+l, j+c) )


for k in mapa.keys():
    #print(k, "->", mapa[k])
    pass
print(start)
print("="*80)

def bfs(mapa:dict, local: tuple, visitados:set = set()) -> int:
    visitados.add( local )
    l, c = local
    # print(local, "->",  mapa[local], arquivo[l][c])
    for vizinho in mapa[local]:
        if vizinho in visitados:
            continue
        return bfs(mapa, vizinho, visitados) + 1
    return 0

print( (bfs(mapa, start) + 1) /2 )
#6968
# ulimit -s 100000000
