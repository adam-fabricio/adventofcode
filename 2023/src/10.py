#!/usr/bin/env python3


import os
import re
import sys
import subprocess


def print_map() -> None:
    for l, line in enumerate(arquivo):
        for c, col in enumerate(arquivo[l]):
            if (l, c) in visitados:
                print("\033[0;32;40m", end="")
                print(col, end="")
                print("\033[0m", end="")
            elif (l, c) in inner:
                print("\033[0;31;40m", end="")
                print("I", end="")
                print("\033[0m", end="")


            else:
                print(col, end='')
        print()


test = 0
part = "1"
dia = "10"

sys.setrecursionlimit(10**6)
#  ulimit -s 100000000

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

dot = set()
inner = set()
visitados = set()
mapa = {}
out = set()


for l, lines in enumerate(arquivo):
    for c, col in enumerate(lines):
        if col == ".":
            dot.add( (l, c) )
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
                continue
            mapa[(l, c)].append( (i+l, j+c) )




def dfs(mapa:dict, local: tuple) -> int:
    visitados.add( local )
    l, c = local
    for vizinho in mapa[local]:
        if vizinho in visitados:
            continue
        #print_map()
        #print("="*80)
        #input()
        return dfs(mapa, vizinho) + 1
    return 1

print("Parte 1:", ( dfs(mapa, start) ) /2 )
print("="*80)

for l, lin in enumerate(arquivo):
    aux = ""
    count = 0
    for c, col in enumerate(arquivo[l]):
        if (l,c) in visitados:
            if col == "S":
                col = "F"
            if col in "|":
                count += 1
            elif col in "FL":
                aux = col
            elif aux == "F" and col == "J":
                count += 1
                aux = ""
            elif aux == "L" and col == "7":
                count += 1
                aux = ""
        else:
            if count % 2 == 1:
                inner.add( (l, c) )
        #input( f'({l},{c})col: {col} count: {count} aux: {aux}' )

print("Parte 2:", len(inner))

dl = []
dc = []
for l, c in mapa[start]:
    dl.append(l - start[0])
    dc.append(c - start[1])

print(dl, dc)
print(start)
print(mapa[start])

