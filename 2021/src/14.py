#!/usr/bin/env python3

import os


nome_arquivo = "14.in"
local = "assets"
part = "1"

with open(os.path.join(local, nome_arquivo)) as arquivo:
    arquivo = arquivo.read()

raw_template, instrucoes = arquivo.split("\n\n")

instrucao = {linha.split("->")[0].strip(): linha.split("->")[1].strip() \
        for linha in instrucoes.splitlines() }

template = list(raw_template)

def processo(template: list, instrucao: dict) -> list:
    t_copia = template.copy()
    j=1
    for i in range(len(template) - 1):
        par = "".join([template[i], template[i+1]])
        val = instrucao[par]
        t_copia.insert(i+j, val)
        j+=1
    return t_copia



for _ in range(10):
    template = processo(template, instrucao)

itens = { str(template.count(letra)): letra for letra in set(template) }

mais_comum = sorted(map(int, itens.keys()))[-1]
menos_comum = sorted(map(int, itens.keys()))[0]

print(f'parte 1: {mais_comum - menos_comum}')


letras = {}
for letra in raw_template:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1

pares = {}
for i in range(len(raw_template) - 1):
    par = raw_template[i:i+2] 
    if par in pares:
        pares[par] += 1
    else:
        pares[par] = 1


for i in range(40):
    pares_copy = pares.copy()
    pares = {}
    for par in pares_copy:
        nova_letra = instrucao[par]
        if nova_letra in letras:
            letras[nova_letra] += pares_copy[par]
        else:
            letras[nova_letra] = pares_copy[par]

        novo_pares = [par[0]+nova_letra, nova_letra+par[1]]
        for n_p in novo_pares:
            if n_p in pares:
                pares[n_p] += pares_copy[par]
            else:
                pares[n_p] = pares_copy[par]


num_letras = sorted(letras.values())

print(f'parte_2 = {num_letras[-1] - num_letras[0] }')

