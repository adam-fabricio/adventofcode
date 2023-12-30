#!/usr/bin/env python3


import os
import re
from sys import argv
from collections import deque


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
            and arquivo[n_l][n_c] != "#") > 2}


for v_l, v_c in vertices:
    fila.append((v_l, v_c, 0))
    visitados= {(v_l, v_c)}

    while fila:
        l, c, d = fila.popleft()
        print(l, c)
        if d != 0 and vertices.get((l, c), 0):
            vertices[(v_l, v_c)][(l, c)] = d
            continue

        for n_l, n_c in [(l+1, c), (l-1, c), (l, c+1), (l, c-1)]:
            if (0 <= n_l < l_max and
                    0 <= n_c < c_max and
                    arquivo[n_l][n_c] != "#" and
                    (n_l, n_c) not in visitados):
                fila.append((n_l, n_c, d+1))
                visitados.add((n_l, n_c))

print(vertices)
