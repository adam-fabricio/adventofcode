#!/usr/bin/env python3


import os
import re
from collections import deque
from sys import argv


def trata_outros(entrada: int) -> tuple:
    return (1, entrada) if modulo in modulos else (0, entrada) 


def trata_ff(entrada: int, estado: int) -> tuple:
    return (0, estado) if entrada else (1, not estado)


def trata_inv(entrada: bool) -> tuple:
    return (1, not entrada)


def trata_con(componente: str, entrada: bool) -> tuple:
    modulos[modulo]['inputs'].append((componente, entrada))
    if len(modulos[modulo]['inputs']) == 2:
        logic = not(modulos[modulo]['inputs'][0][1] &
                    modulos[modulo]['inputs'][1][1])
        if logic:
            return (1, logic)
        else:
            return (1, logic)
    else:
        return(0, 0)


def send(tipo: str, componente: str, entrada: int, estado: int) -> int:
    if tipo == "outros":
        return trata_outros(entrada)
    elif tipo == "ff":
        return trata_ff(entrada, estado)
    elif tipo == "inv":
        return trata_inv(entrada)
    elif tipo == "con":
        return trata_con(componente, entrada)



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
        count = 0
        for m in modulos:
            for out in modulos[m]['out']:
                if out == modulo:
                    count += 1
        if count == 1:
            modulos[modulo]['type'] = "inv"
        else:
            modulos[modulo]['type'] = "con"
            modulos[modulo]['inputs'] = []
modulos["botao"] = {'out': ['broadcaster'], 'state': 0}

nivel_baixo = 0
nivel_alto = 0
sequencia = deque()
for i in range(3):
    sequencia.append("botao")
    while sequencia:
        componente = sequencia.popleft()

        for modulo in modulos[componente]['out']:
            #print(send(modulos[modulo]['type'], componente, modulos[componente]['state'], modulos[modulo]['state']))
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
            input(f"{componente} - {modulos[componente]['state']}-> {modulo}")
    print(i, nivel_alto)
    print(i, nivel_baixo)
