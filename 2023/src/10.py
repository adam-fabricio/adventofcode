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

dot = set()
mapa = {}
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
                #print(l,c, arquivo[i+l][j+c])
                continue
            mapa[(l, c)].append( (i+l, j+c) )


for k in mapa.keys():
    #print(k, "->", mapa[k])
    pass
print(start)
print("="*80)

visitados = set()

def dfs(mapa:dict, local: tuple) -> int:
    visitados.add( local )
    l, c = local
    for vizinho in mapa[local]:
        if vizinho in visitados:
            continue
        return dfs(mapa, vizinho) + 1
    return 1

print( ( dfs(mapa, start) ) /2 )
inner = set()
out = set()
for d in dot:
    l, c = d
    if l == 0 or c == 0 or c==(len(arquivo[0])-1) or l == (len(arquivo)-1):
        out.add( (l, c) )
        continue
    for direcoes in [ (0,1), (1,0), (0,-1), (-1,0) ]:
        dl, dc = direcoes
        ll = l + dl
        cc = c + dc
        convert = 0
        while True:
            if (ll, cc) in out:
                out.add( (l, c) )
                convert = 1
                break
            elif (ll == 0 or cc == 0 or cc==(len(arquivo[0])-1)
                  or ll == (len(arquivo)-1)):
                out.add( (l, c) )
                convert = 1
                break
            elif (ll, cc) in visitados:
                inner.add( (l, c) )
                convert = 1
                break
            ll += dl
            cc += dc
        if convert:
            continue




for l, lines in enumerate(arquivo):
    for c, col in enumerate(lines):
        if (l, c)  in visitados:
            print("\033[0;32;40m", end="")
            print(col, end="")
            print("\033[0m", end="")
        elif (l, c) in out:
            print("\033[0;34;31m", end="")
            print("O", end="")
            print("\033[0m", end="")
        elif (l, c) in inner:
            print("\033[0;32;35m", end="")
            print("I", end="")
            print("\033[0m", end="")
        elif (l, c) in dot:
            print("\033[0;33;31m", end="")
            print(col, end="")
            print("\033[0m", end="")

        else:
            print(col, end ="")
    print()

#  6968
#  ulimit -s 100000000
