#!/usr/bin/env python3


import os
import re


test = 0
part = "1"
dia = "08"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().split('\n\n')

inst, maps = arquivo
#{ 0 : {R: 2 1:-1, L:3 :-1
dict_maps = { l.split(" ")[0]: 
             { "L": l.split(" ")[2][1:-1], "R": l.split(" ")[3][:-1]} 
             for l in maps.splitlines() }

position = "AAA"
i = 0
while position != "ZZZ":
    index = i % len(inst)
    position = dict_maps[position][inst[index]]
    i += 1
print("PARTE 1:", i)


positions = [ p for p in dict_maps.keys()
        if re.match("[0-9A-Z][0-9A-Z][A]", p ) ]
ends = [ p for p in dict_maps.keys() if re.match("[0-9A-Z][0-9A-Z][Z]", p ) ]

ans = []
p = positions[0]
for p in positions:
    i = 0
    while True:
        index = i % len(inst)
        p = dict_maps[p][inst[index]]
        i += 1
        if p in ends:
            ans.append(i)
            break

mmc = 1
d = 2
while not all( a == 1 for a in ans):
    c = 0
    for i, a in enumerate(ans):
        if a % d == 0:
            ans[i] = a / d
            if c:
                continue
            c = 1
    if c:
        mmc *= d
        continue
    d += 1

print("parte 2:", mmc)
