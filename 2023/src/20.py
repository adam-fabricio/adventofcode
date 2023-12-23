#!/usr/bin/env python3


import os
import re
from collections import deque
from sys import argv


def trata_outros(entrada: int) -> tuple:
    return (1, entrada)


def trata_ff(entrada: int, estado: bool) -> tuple:
    if entrada:
        return (0, estado)
    else:
        return (1, not estado)


def trata_inv(entrada: bool, estado: bool) -> tuple:
    return (1, not entrada)



def trata_con() -> tuple:

    for status in modulos[modulo]['inputs']:
        if not modulos[status]['state']:
            return (1, True)
    return (1, False)


def send(tipo: str, componente: str, entrada: int, estado: int) -> int:
    if tipo == "outros":
        return trata_outros(entrada)
    elif tipo == "ff":
        return trata_ff(entrada, estado)
    elif tipo == "inv":
        return trata_inv(entrada, estado)
    elif tipo == "con":
        return trata_con()


print('--- Day 20: Pulse Propagation ---')
test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]
if test:
    dia = dia + "_test"
path = os.path.join("data", dia)
with open(path) as f:
    arquivo = f.read().splitlines()

modulos = {i[0] if not i[0][0] in "&%" else i[0][1:]:
           {'out': i[1].split(", "), "state": 0,
           "type": "ff" if i[0][0] == "%" else "conjuction"
            if i[0][0] == "&" else "outros" }
           for item in arquivo
           for i in [item.split(" -> ")]}

for modulo in modulos:
    if modulos[modulo]["type"] == "conjuction":
        modulos[modulo]['inputs'] = []
        count = 0
        for m in modulos:
            for out in modulos[m]['out']:
                if out == modulo:
                    modulos[modulo]["inputs"].append(m)
                    count += 1
        if count == 1:
            modulos[modulo]['type'] = "inv"
        else:
            modulos[modulo]['type'] = "con"
modulos["botao"] = {'out': ['broadcaster'], 'state': 0}


list_part2 = modulos['mf']['inputs']

ans = []
total_alto = 0
total_baixo = 0
sequencia = deque()
j = 0
while True:
    j+=1
    nivel_baixo = 0
    nivel_alto = 0
    sequencia.append("botao")
    while sequencia:
        componente = sequencia.popleft()

        for modulo in modulos[componente]['out']:
            if modulos.get(modulo, 0):
                f, modulos[modulo]['state'] = send(modulos[modulo]['type'],
                                                   componente,
                                                   modulos[componente]['state'],
                                                   modulos[modulo]['state'])
                if f:
                    sequencia.append(modulo)



            if modulos[componente]['state']:
                nivel_alto += 1
            else:
                nivel_baixo += 1

            if componente in list_part2 and modulos[componente]['state']:
                list_part2.remove(componente)
                ans.append(j)

    total_alto += nivel_alto
    total_baixo += nivel_baixo
    if len(ans) == 4:
        break
    if j == 1000:
        print("Parte 1:", total_baixo * total_alto )

d = 2
mmc = 1
while not all( a == 1 for a in ans):
    c = 0
    for i, a in enumerate(ans):
        if a % d == 0:
            ans[i] = a/d
            if c:
                continue
            c = 1
    if c:
        mmc *= d
        continue
    d += 1

print('Parte 2:', mmc)
