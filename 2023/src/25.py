#!/usr/bin/env python3


import heapq
import os
import re
from copy import deepcopy
from random import choice
from sys import argv
from collections import deque


def bfs_subgrafo(grafo, no):
    visitados = set()
    fila = deque()
    fila.append(no)

    while fila:
        no = fila.popleft()
        if no in visitados:
            continue
        visitados.add(no)
        fila.extend(set(grafo[no]) - visitados)
    return len(visitados)


def bfs_ff(grafo:dict, inicio: str, fim: str):
    fila = deque()
    fila.append(inicio)
    caminhos = {inicio: []}

    if inicio == fim:
        return caminhos[inicio]

    while fila:
        v = fila.popleft()

        for u in grafo[v]:
            if u not in caminhos:
                caminhos[u] = caminhos[v] + [v]
                if u == fim:
                    return caminhos[u] + [fim]
                fila.append(u)
    return None


def ford_fulkerson(grafo: dict, no1: str, no2: str) -> tuple:
    fluxo, caminho = 0, True
    arestas = []

    while caminho:
        # Busca usando o bfs
        caminho = bfs_ff(grafo, no1, no2)
        if caminho is None:
            break
        fluxo += 1

        for v, u in zip(caminho[:-1], caminho[1:]):
            if u in grafo[v]:
                grafo[v].remove(u)
                arestas.append((v, u))
            else:
                graph[u].append(v)
    return fluxo, len(arestas), arestas



def dijkstra(grafo: dict, inicio: str) -> dict:
    distancia = {no: 10**4 for no in grafo}
    distancia[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        dist_atual, no_atual = heapq.heappop(fila)

        #if dist_atual != distancia[no_atual]:
        #    continue

        for vizinho in grafo[no_atual]:
            nova_distancia = dist_atual + 1

            if nova_distancia < distancia[vizinho]:
                distancia[vizinho] = nova_distancia
                heapq.heappush(fila, (nova_distancia, vizinho))
    return(distancia)


def maior_distancia(d: dict) -> tuple:
    no = max(d, key=d.get)
    return (no, d[no])


def remover_aresta(g:dict, no1: str, no2: str) -> dict:
    grafo = deepcopy(g)
    grafo[no1].remove(no2)
    grafo[no2].remove(no1)
    return grafo


def bfs(grafo, inicio, fim):
    visitados = set()
    fila = deque()
    fila.append(inicio)

    while fila:
        no = fila.popleft()

        if no == fim:
            return True

        if no in visitados:
            continue
        visitados.add(no)

        vizinhos = grafo[no]
        fila.extend(vizinho for vizinho in vizinhos if vizinho not in visitados)
    return False


def karger(grafo: dict) -> int:
    grafo_2 = deepcopy(grafo)
    cortes = []

    while len(grafo_2) > 2:
        v = choice(list(grafo_2.keys()))
        w = choice(grafo_2[v])
        cortes.append((v, w))
        contracao(grafo_2, v, w)

    subgrafos = {no: [vizinho for vizinho in vizinhos if vizinho in grafo_2] for no, vizinhos in grafo_2.items()}
    return len(next(iter(grafo_2.values()))), cortes, subgrafos


def contracao(grafo: dict, v: str, w:str) -> None:
    for no in grafo[w]:
        if no != v:
            grafo[v].append(no)
        grafo[no].remove(w)
        if no != v:
            grafo[no].append(v)
    del grafo[w]


test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

grafo = {}
for line in  arquivo:
    grupo = re.findall("[a-zA-Z]{3}", line)
    for no in grupo[1:]:
        if not grafo.get(grupo[0], 0):
            grafo[grupo[0]] = []
        grafo[grupo[0]].append(no)
        if not grafo.get(no, 0):
            grafo[no] = []
        grafo[no].append(grupo[0])

#combinacoes = {tuple(sorted((no, vizinho))) for no, vizinhos in grafo.items()
#        for vizinho in vizinhos}

ans = []
for _ in range(100):
    n, cortes, subgrafos = karger(grafo)
    ans.append(n)
    if n == 3:
        break

distancias = {}
for no in grafo:
    no_longe = maior_distancia(dijkstra(grafo, no))
    distancias[(no, no_longe[0])] = no_longe[1]

nos_distantes = maior_distancia(distancias)
inicio = nos_distantes[0][0]
fim = nos_distantes[0][1]


ford_fulkerson(grafo, inicio, fim)

a = bfs_subgrafo(grafo, inicio)
b = bfs_subgrafo(grafo, fim)

print("--- Day 25: Snowverload ---")
print("Parte 1:", a * (b - a))

