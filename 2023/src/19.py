#!/usr/bin/env python3


import os
import re
from sys import argv
from collections import deque

test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]
if test:
    dia = dia + "_test"

path = os.path.join("data", dia)
with open(path) as f:
    arquivo = f.read().split("\n\n")

workflow = {chave: [[item
                     for item in v.split(":")]
                    for v in valor[:-1].split(",") ]
            for linha in arquivo[0].splitlines()
            for chave, _, valor in [linha.partition("{")]}

parts = [{r: int(val)
          for item in linha[1:-1].split(",")
          for r, val in [item.split('=') ]}
         for linha in arquivo[1].splitlines()]

ans = 0

for n, part in enumerate(parts):
    flow = "in"
    while not flow in "AR":
        flag = 0
        for i in range(len(workflow[flow])-1):
            r = workflow[flow][i][0][0]
            op = workflow[flow][i][0][1]
            val = int(workflow[flow][i][0][2:])
            n_flow = workflow[flow][i][1]
            if op == "<":
                if part[r] < val:
                    flow = n_flow
                    flag = 1
                    break
            else:
                if part[r] > val:
                    flow = n_flow
                    flag = 1
                    break
        if not flag:
            flow = workflow[flow][-1][0]
    if flow == "A":
        for p in part:
            ans += part[p]

print("Parte 1:", ans)

#-------------------------------------------------------------------------------

range_parts = { a: [1, 4000] for a in ['x', 'm', 'a', 's'] }
fila = deque()
fila.append( ("in", range_parts) )

ans = 0
while fila:
    flow, range_parts = fila.pop()

    if flow == "R":
        continue
    elif flow == "A":
        aux = 1
        for p in range_parts:
            aux *= range_parts[p][1] - range_parts[p][0] + 1
        ans += aux
        continue


    for i in range(len(workflow[flow])-1):
        r = workflow[flow][i][0][0]
        op = workflow[flow][i][0][1]
        val = int(workflow[flow][i][0][2:])
        n_flow = workflow[flow][i][1]

        if op == "<":
            if range_parts[r][0] > val-1:
                continue
            n_range = [ range_parts[r][0], val - 1 ]
            c_range = [ val, range_parts[r][1] ]
        else:
            if val+1 > range_parts[r][1]:
                continue
            n_range = [ val + 1, range_parts[r][1] ]
            c_range = [ range_parts[r][0], val ]

        n_range_parts = range_parts.copy()
        n_range_parts[r] = n_range
        fila.append((n_flow, n_range_parts))

        range_parts[r] = c_range

    fila.append((workflow[flow][-1][0], range_parts))

print("Parte 2:", ans)
