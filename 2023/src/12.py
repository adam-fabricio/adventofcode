#!/usr/bin/env python3


import os
import re
from functools import cache

test = 0
part = "1"
dia = "12"

@cache
def padroes(record, grupos):
    ans = 0
    padrao = r"(?=((?<!#)[#?]{{{n}}}(?!#)))".format(n=grupos[0])
    resultado = re.finditer(padrao, record)
    for seq in resultado:
        if "#" in record[:seq.start(1)]:
            continue
        #print(f"{grupos[0]} -> {record} -> {seq.group(1)} -> {seq.span(1)}")
        if len(grupos) == 1:
            if "#" in record[seq.end(1)+1:]:
                continue
            else:
                ans += 1
        else:
            ans += padroes(record[seq.end(1)+1:], grupos[1:])
    return ans



if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

ans1 = 0
for i, item in enumerate(arquivo):
    records, groups = item.split(" ")
    list_groups = tuple(map(int, groups.split(",")))
    ans1 += padroes(records, list_groups)


ans2 = 0
for i, item in enumerate(arquivo):
    records, groups = item.split(" ")
    records = "?".join([records]*5)
    groups = ",".join([groups] * 5 )
    list_groups = tuple(map(int, groups.split(",")))
    ans2 += padroes(records, list_groups)

print("parte 1:", ans1)
print("parte 2:", ans2)


