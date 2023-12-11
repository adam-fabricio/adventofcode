#!/usr/bin/env python3


import os
import re


test = 0
part = "1"
dia = "11"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

arquivo_2 = arquivo.copy()

add_col = []
for col in range(len(arquivo[0])):
    if all( char == "." for line in arquivo for char in line[col]):
        add_col.append(col)
add_lin = []
for l, line in enumerate(arquivo):
    if all( char == "." for char in line):
        add_lin.append( l )
acc = 0
for c in add_col:
    for l in range(len(arquivo)):
        arquivo[l] = arquivo[l][:c+acc] + "." + arquivo[l][c+acc:]
    acc += 1

acc = 0
for l in add_lin:
    arquivo.insert(l+acc, "." * len(arquivo[l]) )
    acc += 1

i = 1
galaxy = []
for l, lin in enumerate(arquivo):
    for c, col in enumerate(arquivo[l]):
        if col == "#":
            i += 1
            galaxy.append( (i, l, c) )

distance = []
sum_galaxy = set()
for i, l, c in galaxy:
    for ii, ll, cc in galaxy:
        if (i, ii) in sum_galaxy:
            continue
        sum_galaxy.add( (i, ii) )
        sum_galaxy.add( (ii, i) )
        distance.append( abs(l - ll) + abs(c - cc) )

print("Parte 1:",sum(distance))


i = 1
galaxy = []
for l, lin in enumerate(arquivo_2):
    for c, col in enumerate(arquivo_2[l]):
        if col == "#":
            galaxy.append( (i, l, c) )
            i += 1

fator_c = 10**6 - 1
distance = []
sum_galaxy = set()
for i, l, c in galaxy:
    for ii, ll, cc in galaxy:
        if (i, ii) in sum_galaxy:
            continue
        sum_galaxy.add( (i, ii) )
        sum_galaxy.add( (ii, i) )
        fator = 0
        for exp_lin in add_lin:
            if l < exp_lin and ll > exp_lin:
                fator += fator_c
            elif ll < exp_lin and l > exp_lin:
                fator += fator_c
        for exp_col in add_col:
            if c < exp_col and cc > exp_col:
                fator += fator_c
            elif cc < exp_col and c > exp_col:
                fator += fator_c
        d = abs(l - ll) + abs(c - cc) + fator
        distance.append( abs(l - ll) + abs(c - cc) + fator )


print("Parte 2:", sum(distance))

