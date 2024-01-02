#!/usr/bin/env python3


import os
import re


test = False
part = "1"
dia = "02"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read()

jogos = {}
for line in arquivo.splitlines():
    id_game, games = line.split(":")
    id_game = id_game.split(" ")[1]
    
    bags = {i: { cube.split(" ")[1]: int(cube.split(" ")[0])
                for cube in cubes.strip().split(", ")}
            for i, cubes in enumerate(games.split(";"))}

    jogos[int(id_game)] = bags

resultado = []
for jogo in jogos:
    skip = False
    for bag in jogos[jogo]:
        if jogos[jogo][bag].get("red", 0) > 12:
            skip = True
            break
        if jogos[jogo][bag].get("green", 0) > 13:
            skip = True
            break
        if jogos[jogo][bag].get("blue", 0) > 14:
            skip = True
            break
    if skip:
        continue
    resultado.append(jogo)

print(f'parte 1: {sum(resultado)}')

parte_2 = []
for jogo in jogos:
    red = 0
    green = 0
    blue = 0
    for bag in jogos[jogo]:
        if jogos[jogo][bag].get("red", 0) > red:
            red = jogos[jogo][bag].get("red", 0)
        if jogos[jogo][bag].get("green", 0) > green:
            green = jogos[jogo][bag].get("green", 0)
        if jogos[jogo][bag].get("blue", 0) > blue:
            blue = jogos[jogo][bag].get("blue", 0)
    parte_2.append(red * green * blue)
print(sum(parte_2))

