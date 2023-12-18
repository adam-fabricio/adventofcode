#!/usr/bin/env python3


import os
import re
from sys import argv
from queue import PriorityQueue



def h(a:tuple) ->int:
    media = sum (sum(l) for l in grid) / (l_max * c_max)
    return l_max - a[0] + c_max - a[1]


test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]
if test:
    dia = dia + "_test"

path = os.path.join("data", dia)
with open(path) as f:
    arquivo = f.read().splitlines()

n=1
l_max = len(arquivo)
c_max = len(arquivo[0])
grid = [[ int(c) for c in linha] for linha in arquivo]
direcoes = [(0, 1), (1, 0), (0,-1), (-1, 0)]
inicio = (0, 0)
vetor = (0, 0)
final = (l_max-1, c_max-1)
custo_inicial = 0

visitados = set()
fila = PriorityQueue()
fila.put((0 + h(inicio), custo_inicial, inicio, vetor, n))

predecessores = {}
vetores = {}

while not fila.empty():
    prioridade, custo, pos, vetor, n = fila.get()
    #print(prioridade, custo, pos, vetor, n)

    visitados.add((pos, vetor, n))
    if pos == final:
        break

    for d in direcoes:
        nl = pos[0] + d[0]
        nc = pos[1] + d[1]
        n_pos = (nl, nc)
        if nl in [l_max, -1] or nc in [c_max, -1]:
            continue
        if d == vetor:
            n+=1
            if n > 3:
                continue
        else:
            n = 1
        if (n_pos, d, n) in visitados:
            continue

        g = custo + grid[nl][nc]
        f = g + h(n_pos)

        i_f = [ i for i, n in enumerate(fila.queue) if (n[2], n[3], n[4] ) == (n_pos, d, n) ]

        if i_f:
            if g < fila.queue[i_f[0]][1]:
                #  prioridade, custo, pos, vetor, n = fila.get()
                fila.queue[i_f[0]] = (f, g, n_pos, d, n)
        else:
            fila.put((f, g, n_pos, d, n))
        predecessores[n_pos] = g
        vetores[n_pos] = d

print(predecessores[final])
