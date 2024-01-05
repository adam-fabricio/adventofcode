#!/usr/bin/env python3


from heapq import heappush, heappop
from time import sleep
from os import system


def print_map():
    # Cores texto

    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    F_BLACK = '\033[40m'
    F_RED = '\033[41m'
    F_GREEN = '\033[42m'
    F_YELLOW = '\033[43m'
    F_BLUE = '\033[44m'
    F_MAGENTA = '\033[45m'
    F_CYAN = '\033[46m'
    F_WHITE = '\033[47m'
    print('\033[0;0H', end='')
    print("=" * 80)
    for p_l in range(l_max):
        for p_c in range(c_max):
            if (l, c) == (p_l, p_c):
                print(RED, end='')
            elif (p_l, p_c) in visitados:
                print(F_BLUE, WHITE, sep='',  end='')
            print(mapa[p_l][p_c], end=' ')
            print(RESET, end='')
        print()
    print("=" * 80)
    return
    for p_l in range(l_max):
        for p_c in range(c_max):
            valor = distancias[p_l][p_c]
            print(valor if valor < 10000 else 'X' , end='\t')
        print()
    print("=" * 80)




mapa = [list(map(int,linha.strip())) for linha in open(0)]

r = 15
l_max = len(mapa)
c_max = len(mapa[0])

inicio = (0, 0, 0, 0)
final  = (l_max - 1, c_max - 1, r-1, r-1)


distancias = [[10**6 for _ in range(c_max * r)] for _ in range(l_max * r)]

fila = []
custo = 0

distancias[0][0] = 0
visitados = set()

heappush(fila, (0, inicio) )

nos = 0
comparacoes =0

while fila:
    custo, (l, c, ml, mc) = heappop(fila)

    # Marcar como visitado
    if (l, c, ml, mc) in visitados:
        continue
    visitados.add((l, c, ml, mc))


    for n_l, n_c in [(l+1, c), (l-1, c), (l, c+1), (l, c-1)]:
        n_ml = ml
        n_mc = mc
        if n_l < 0:
            if ml <= 0:
                continue
            else:
                n_ml = ml - 1
                n_l = l_max - 1
        elif n_l == l_max:
            if ml == r - 1:
                continue
            else:
                n_ml = ml + 1
                n_l = 0
        if n_c < 0:
            if mc <= 0:
                continue
            else:
                n_mc = mc - 1
                n_c = c_max - 1
        elif n_c == c_max:
            if mc == r - 1:
                continue
            else:
                n_mc = mc + 1
                n_c = 0
        elif (n_l, n_c, n_ml, n_mc) in visitados:
            continue

        custo_aresta = mapa[n_l][n_c] + n_ml + n_mc
        if custo_aresta >= 10:
            custo_aresta = custo_aresta % 10 + custo_aresta // 10
        n_custo = custo_aresta + custo
        if n_custo < distancias[n_l + n_ml * l_max][n_c + n_mc * c_max]:
            heappush(fila, (n_custo, (n_l, n_c, n_ml, n_mc)))
            distancias[n_l + n_ml * l_max][n_c + n_mc * c_max] = n_custo


print(f"--- Day 15: Chiton --- Implementado com Dijkstra --- {r} mapas ---")
print("Parte 1:", distancias[l_max-1][c_max-1])
print("Parte 2:", distancias[-1][-1])
