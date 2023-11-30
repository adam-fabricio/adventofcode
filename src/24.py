#!/usr/bin/env python3

import os


nome_arquivo = "24_test.in"
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


print(raw_template)

templates = [ raw_template ]
a = []
for i in range(20):
    templates.append( ''.join(processo(list(templates[i]), instrucao)))
    
    if templates[i] in templates[i+1]:
        break

print(i)

#print(templates[i] )

#print(templates[i+1])
