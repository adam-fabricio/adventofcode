#!/usr/bin/env python3


import os
import re
from sys import argv, setrecursionlimit
from collections import deque
from functools import cache


setrecursionlimit(10**6)

def dfs(vertice):
    if vertice == final:
        return 0

    m = -10000

    visitados.add(vertice)
    for n_vertice in vertices[vertice]:
        if n_vertice not in visitados:
            m = max(m, dfs(n_vertice) + vertices[vertice][n_vertice])
            #print(m)
    visitados.remove(vertice)
    return m

ans = []
def dfs_p(vertice, d=0):
    if vertice in visitados:
        return
    visitados.add(vertice)

    if vertice == final:
        ans.append(d)
    for n_v in vertices[vertice]:
        dfs_p(n_v, d+vertices[vertice][n_v])
    visitados.remove(vertice)





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

inicio = (0, 1)
versor = (1, 0)
d_0 = 0

final = (l_max-1, c_max-2)

fila = deque()

vertices = {}

vertices = {(l, c): {} for l, line in enumerate(arquivo)
        for c, col, in enumerate(line) if
        col != "#" and sum(1
            for n_l, n_c in [(l - 1, c), (l + 1, c), (l, c - 1), (l, c + 1)]
            if 0 <= n_l < l_max and 0 <= n_c < c_max
            and arquivo[n_l][n_c] != "#") != 2}


for v_l, v_c in vertices:
    fila.append((v_l, v_c, 0))
    visitados= {(v_l, v_c)}

    while fila:
        l, c, d = fila.popleft()
        if d != 0 and (l, c) in vertices.keys():
            vertices[(v_l, v_c)][(l, c)] = d
            vertices[(l, c)][(v_l, v_c)] = d
            continue

        for n_l, n_c in [(l+1, c), (l-1, c), (l, c+1), (l, c-1)]:
            if (0 <= n_l < l_max and
                    0 <= n_c < c_max and
                    arquivo[n_l][n_c] != "#" and
                    (n_l, n_c) not in visitados):
                fila.append((n_l, n_c, d+1))
                visitados.add((n_l, n_c))
visitados = set()
#dfs_p(inicio)

fila = deque
fila.append((inicio, 0, visitados))

while fila:
    vertice, d, visitado = fila.pop()

    if vertice in visitado:
        continue
    if vertice == final:
        ans.append(d)

    for nv in vertices[vertice]:
        fila.append((nv, d+vertices[vertice][nv], {}.union({(vertice)})))

print(max(ans))
