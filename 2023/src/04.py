#!/usr/bin/env python3


import os
import re


test = 0
part = "1"
dia = "04"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

games = [ game.split(":")[1].split("|") for game in arquivo ]

ans = 0
for game in games:
    points = 0
    for number in game[1].strip().split():
        if number in game[0].strip().split():
            points += 1
    if points >= 1:
        ans += 2 ** (points - 1)

print(ans)
