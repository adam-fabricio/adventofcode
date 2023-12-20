#!/usr/bin/env python3


import os
import re
from collections import deque
from sys import argv


test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()
comandos = [ (item[0], int(item[1])) for item in map(str.split, arquivo) ]


pos = (0, 0)
visitados = set()
visitados.add(pos)
for d, v in comandos:
    if d == 'R':
        l, c = 0, 1
    elif d == 'D':
        l, c = 1, 0
    elif d == 'L':
        l, c = 0, -1
    elif d == 'U':
        l, c = -1, 0

    for _ in range(v):
        pos = (pos[0] + l, pos[1] + c)
        visitados.add(pos)

l = [x[0] for x in visitados]
c = [x[1] for x in visitados]

l_max = max(l)
l_min = min(l)
c_max = max(c)
c_min = min(c)
half_point = (int((l_max+l_min)/2), int((c_max+c_min)/2))
fila = deque()
fila.append(half_point)
fill = set()
while fila:
    l, c = fila.pop()
    fill.add((l, c))

    for dl, dc in [(1, 0), (0, 1), (-1, 0), (0, -1) ]:
        n_pos = (dl+l, dc+c)
        if n_pos in visitados or n_pos in fill:
            continue
        fila.append(n_pos)

print(f"Parte 1: {len(visitados)+len(fill)}")

direction = {'0': (0, 1), '1': (1, 0), '2': (0, -1), '3': (-1, 0)}
comandos2 = [ (direction[item[-1][-2]], int(item[-1][-7:-2], base=16))
        for item in map(str.split, arquivo) ]

visitados = []
pos = (0,0)
visitados.append(pos)

b = 0

for d, v in comandos2:
    b+=v
    pos = (pos[0]+d[0]*(v), pos[1]+d[1]*(v))
    visitados.append(pos)

ans = []
for i in range(len(visitados)-1):
    ans.append(visitados[i][0] * visitados[i+1][1] -
            (visitados[i+1][0] * visitados[i][1]) )

res = int(abs(sum(ans)/2))
res1 = int(b/2)

resultado = res+res1+1



print("Parte 2:", resultado)
