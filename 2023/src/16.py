#!/usr/bin/env python3


import os
import re
from sys import argv
from collections import deque


def reflect(d: str, vetor:tuple) -> tuple:
    if d == "h":
        a = vetor[1]
        b = -vetor[0]
    else:
        a = -vetor[1]
        b = vetor[0]
    return (a, b)


def print_map(v:set)->None:
    os.system('clear')
    for l in range(l_max):
        for c in range(c_max):
            if (l,c) in v:
                print("#", end='')
            else:
                print(".", end='')
        print()
    print("=" * 80)


test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

l_max = len(arquivo)
c_max = len(arquivo[0])

grid = [ [c for c in linha ] for linha in arquivo ]


starts = []
for l in range(l_max):
    starts.append(((l,0),(0,1)))
    starts.append(((l,c_max-1),(0,-1)))
for c in range(c_max):
    starts.append(((0,c),(1,0)))
    starts.append(((l_max-1,c),(-1,0)))

ans = []
for start in starts:
    # start
    fila = deque()
    fila.append(start)
    visitados = set()
    energized = set()
    while fila:
        versor = fila.popleft()
        posicao, direcao = versor
        p_l, p_c = posicao
        d_l, d_c = direcao

        if p_l in [l_max, -1] or p_c in [c_max, -1]:
            continue
        energized.add(posicao)
        if versor not in visitados:
            visitados.add(versor)
            if grid[p_l][p_c] == ".":
                fila.append(((p_l+d_l, p_c+d_c), (d_l, d_c)))
            elif grid[p_l][p_c] == "\\":
                if not d_l:
                    d_l, d_c = reflect("h", direcao)
                else:
                    d_l, d_c = reflect("ah", direcao)
                fila.append(((p_l+d_l, p_c+d_c), (d_l, d_c)))
            elif grid[p_l][p_c] == "/":
                if not d_c:
                    d_l, d_c = reflect("h", direcao)
                else:
                    d_l, d_c = reflect("ah", direcao)
                fila.append(((p_l+d_l, p_c+d_c), (d_l, d_c)))
            elif grid[p_l][p_c] == "-":
                if not d_l:
                    fila.append(((p_l+d_l, p_c+d_c), (d_l, d_c)))
                else:
                    d_l, d_c = reflect("h", direcao)
                    fila.append(((p_l+d_l, p_c+d_c), (d_l, d_c)))
                    d_l, d_c = reflect("ah", direcao)
                    fila.append(((p_l+d_l, p_c+d_c), (d_l, d_c)))
            elif grid[p_l][p_c] == "|":
                if not d_c:
                    fila.append(((p_l+d_l, p_c+d_c), (d_l, d_c)))
                else:
                    d_l, d_c = reflect("h", direcao)
                    fila.append(((p_l+d_l, p_c+d_c), (d_l, d_c)))
                    d_l, d_c = reflect("ah", direcao)
                    fila.append(((p_l+d_l, p_c+d_c), (d_l, d_c)))
            #input(f"fila: {fila}")
    #print(len(energized))
    ans.append(len(energized))
#print(ans)

print("--- Day 16: The Floor Will Be Lava ---")
print("Parte 1:", ans[0])
print("parte 2:", max(ans))




