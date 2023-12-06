#!/usr/bin/env python3


import os
import re


test = 0
part = "2"
dia = "05"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().split("\n\n")

seeds = [ int(s) for s in arquivo[0].split(":")[1].strip().split(" ") ]

tabela = [ sorted([[b, a, c] for s in a.splitlines()[1:]
    for a, b, c in [map(int, s.split(" "))]],key=lambda x: x[0])
    for a in arquivo[1:] ]

convert = [ seeds ]

for j in range(len(tabela)):
    convert.append([])

    for item in convert[j]:
        c = 0
        for i in range(len(tabela[j])):
            if c:
                continue
            item_start, convert_start, range_size = tabela[j][i]
            if item >= item_start and item <= item_start + range_size:
                convert[j+1].append( item - item_start + convert_start )
                c = 1
        if not c:
            convert[j+1].append(item)

print(f'parte 1: {min(convert[-1])}')


range_seeds = [ [seeds[a], seeds[a] + seeds[a+1] - 1] for a in range(0, len(seeds), 2) ]

range_seeds.sort(key=lambda x: x[0])


convert = [ range_seeds ]

for t, tab in enumerate(tabela):
    conv_aux = []
    for item in convert[t]:
        c = 0
        x_min, x_max = item
        for orig, dest, size in tab:
            if c:
                continue

            if x_min > orig + size:
                continue

            if x_max < orig:
                conv_aux.append([ x_min, x_max ] )
                c = 1
                continue

            if x_min < orig:
                conv_aux.append([ x_min, orig - 1 ] )
                x_min = orig

            if x_max < orig + size:
                conv_aux.append( [x_min - orig + dest, x_max - orig + dest] )
                c = 1
                continue

            if x_max >= orig + size:
                conv_aux.append( [x_min - orig +  dest, dest + size - 1 ] )
                x_min = orig + size
        if not c:
            conv_aux.append( [ x_min, x_max ] )
    convert.append( sorted(conv_aux, key=lambda x: x[0] ))
    if t == 12:
        break

print(f'parte 2: {convert[-1][0][0]}')
