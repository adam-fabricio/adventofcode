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
jogos = [ 1 for game in range(len(games)+1) ]

ans = 0
for i, game in enumerate(games, 1):
    points = 0
    for number in game[1].strip().split():
        if number in game[0].strip().split():
            points += 1
    if points >= 1:
        ans += 2 ** (points - 1)
        for dup in range(i+1, i+points+1):
            if dup >= len(jogos):
                continue
            jogos[dup] += jogos[i]

print("parte 1:", ans)

print("parte 2:", sum(jogos[1:]))
