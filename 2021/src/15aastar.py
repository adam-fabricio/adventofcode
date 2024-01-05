#!/usr/bin/env python3


from heapq import heappush, heappop
from time import sleep
from os import system


def print_map(cordenadas, custo):
    l, c = cordenadas
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
            elif (p_l, p_c, 0, 0) in custo.keys():
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


def heuristica(no: tuple) -> float:
    delta_linha  = abs(n_m * final[0] - (no[0] + l_max * no[2]))
    delta_coluna = abs(n_m * final[1] - (no[1] + c_max * no[3]))

    return delta_linha + delta_coluna

def a_estrela():
    fila = []
    heappush(fila, (0, inicio))

    origem = {}
    custo  = {}

    origem[inicio] = None
    custo[inicio] = 0

    while fila:
        posicao = heappop(fila)[1]
        (l, c, ml, mc) = posicao

        if posicao == final:
            break

        for n_l, n_c in [(l + 1, c), (l - 1, c), (l, c + 1), (l, c - 1)]:
            n_ml = ml
            n_mc = mc

            if n_l < 0:
                if ml <= 0:
                    continue
                else:
                    n_ml = ml - 1
                    n_l = l_max - 1
            elif n_l == l_max:
                if ml == n_m - 1:
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
                if mc == n_m - 1:
                    continue
                else:
                    n_mc = mc + 1
                    n_c = 0

            nova_posicao = (n_l, n_c, n_ml, n_mc)
            custo_vizinho = mapa[n_l][n_c] + n_ml + n_mc
            if custo_vizinho >= 10:
                custo_vizinho = custo_vizinho % 10 + custo_vizinho // 10
            novo_custo = custo[posicao] + custo_vizinho

            if nova_posicao not in custo or novo_custo < custo[nova_posicao]:
                custo[nova_posicao] = novo_custo
                prioridade = novo_custo +  heuristica(nova_posicao)
                heappush(fila, (prioridade, nova_posicao))
                origem[nova_posicao] = posicao

                print_map((l, c), custo)

    return origem, custo



mapa = [list(map(int,linha.strip())) for linha in open(0)]

n_m = 1
l_max = len(mapa)
c_max = len(mapa[0])

inicio = (0, 0, 0, 0)
final  = (l_max - 1, c_max - 1, n_m - 1, n_m - 1)

origem, custo = a_estrela()

#print(origem)
print("=" * 80 )

print(f"--- Day 15: Chiton --- Implementado com A* --- {n_m} mapas ---")
#print("Parte 1:", distancias[l_max-1][c_max-1])
print("Parte 2:", custo[(final)])
