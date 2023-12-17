#!/usr/bin/env python3


import os
import re
from sys import argv


def calc_hash(val: str) -> int:
    hash_val = 0
    for char in val:
        if char == "\n":
            continue
        hash_val = ( 17 * (hash_val + ord(char) ) ) % 256
    return hash_val

test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().split(",")

ans = 0
for item in arquivo:
    acc = 0
    for char in item:
        if char == "\n":
            continue
        acc = (17 * (acc +  ord(char))) % 256
    #print(item, acc)
    ans += acc

print("Parte 1:", ans)



boxs = {}
for item in arquivo:
    box = re.match("(?P<lente>[a-zA-Z]+)(?P<oper>[=-])(?P<val>\d*)", item)
    box_dict = box.groupdict()

    box_id = calc_hash(box_dict['lente'])

    if box_dict["oper"] == "=":
        if not boxs.get(box_id):
            boxs[box_id] = {}
        boxs[box_id][f"{box_dict['lente']}"] = box_dict['val']
    else:
        if not boxs.get(box_id):
            continue
        if boxs[box_id].get(box_dict['lente']):
            boxs[box_id].pop(box_dict['lente'])
    #input(f"{boxs}")
ans = 0
for box in boxs:
    count = 1
    for item in boxs[box]:
        i = calc_hash(item)
        ans += (int(box) + 1 ) * count * int(boxs[box][item])
        count += 1
print("Parte 2:", ans)
