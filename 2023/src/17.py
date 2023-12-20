#!/usr/bin/env python3


import os
import re
from sys import argv
from queue import PriorityQueue



def h(a:tuple, custo: int) ->int:
    return custo - a[0] - a[1]


def passo(custo: int, pos: tuple, vetor: tuple, n:int) -> None:
    #print(pos, vetor, n, custo)
    if not pos[0] in [l_max, -1] and not pos[1] in [c_max, -1]:
        fila.put((h(pos, custo), custo+grid[pos[0]][pos[1]], pos, vetor, n))
    #print(prioridade, custo, pos, vetor, n)


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
inicio = (0, 0)
vetor = (0, 1)
final = (l_max-1, c_max-1)
custo_inicial = 0
visitados = set()
fila = PriorityQueue()
fila.put((0 + h(inicio, 0), custo_inicial, inicio, vetor, n))

while not fila.empty():
    prioridade, custo, pos, vetor, n = fila.get()
    #print(prioridade, custo, pos, vetor, n)

    if pos == final:
        break

    if (pos, vetor, n) in visitados:
        continue
    visitados.add((pos, vetor, n))

    #def passo(custo: int, pos: tuple, vetor: tuple, n:int) -> None:
    if n < 3:
        passo(custo, (pos[0]+vetor[0], pos[1]+vetor[1]), vetor, n+1)
    # rotate 90° (a, b) -> (-b, a)
    passo(custo, (pos[0]-vetor[1], pos[1]+vetor[0]), (-vetor[1], vetor[0]), 1)
    # rotate -90° (a, b) -> (-b, a)
    passo(custo, (pos[0]+vetor[1], pos[1]-vetor[0]), (vetor[1], -vetor[0]), 1)
    #input(f"{fila.queue}")
print(custo)


n=0
l_max = len(arquivo)
c_max = len(arquivo[0])
grid = [[ int(c) for c in linha] for linha in arquivo]
inicio = (0, 0)
vetor = (0, 1)
final = (l_max-1, c_max-1)
custo_inicial = 0
visitados = set()
fila = PriorityQueue()
fila.put((0 + h(inicio, 0), custo_inicial, inicio, vetor, n))

while not fila.empty():
    prioridade, custo, pos, vetor, n = fila.get()
    #print(prioridade, custo, pos, vetor, n)

    if pos == final and n>=4:
        break

    if (pos, vetor, n) in visitados:
        continue
    visitados.add((pos, vetor, n))

    #def passo(custo: int, pos: tuple, vetor: tuple, n:int) -> None:
    if n < 10 :
        passo(custo, (pos[0]+vetor[0], pos[1]+vetor[1]), vetor, n+1)

    if n >= 4:
        # rotate 90° (a, b) -> (-b, a)
        passo(custo, (pos[0]-vetor[1], pos[1]+vetor[0]),
                (-vetor[1], vetor[0]), 1)
        # rotate -90° (a, b) -> (-b, a)
        passo(custo, (pos[0]+vetor[1], pos[1]-vetor[0]),
                (vetor[1], -vetor[0]), 1)

print(custo, n)
