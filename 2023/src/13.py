#!/usr/bin/env python3


import os
import re


test = 0
part = "1"
dia = "13"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().split("\n\n")

val = 0
for m, mirror in enumerate(arquivo):
    lines = [ l for l in mirror.splitlines() ]

    max_lines = len(lines)
    max_col = len(lines[0])

    # Simetria vertical
    for s in range(1, max_col):
        simetria = True
        for i in range(max_col):
            left = s - i - 1
            right = s + i
            if right >= max_col or left < 0:
                val += s
                break
            for l in range(max_lines):
                if lines[l][left] != lines[l][right]:
                    simetria = False
                    break
            if not simetria:
                break
        if simetria:
            break
    for s in range(1, max_lines):
        simetria = True
        for i in range(max_lines):
            cima = s - i - 1
            baixo = s + i
            if baixo >= max_lines or cima < 0:
                val += 100 * s
                break
            for c in range(max_col):
                if lines[cima][c] != lines[baixo][c]:
                    simetria = False
                    break
            if not simetria:
                break
        if simetria:
            break

val1 = 0
for m, mirror in enumerate(arquivo):
    lines = [ l for l in mirror.splitlines() ]

    max_lines = len(lines)
    max_col = len(lines[0])
    # Simetria vertical
    for s in range(1, max_col):
        erros = 0
        for i in range(max_col):
            left = s - i - 1
            right = s + i
            if right >= max_col or left < 0:
                break
            for l in range(max_lines):
                if lines[l][left] != lines[l][right]:
                    erros += 1
        if erros ==  1:
            val1 += s

    for s in range(1, max_lines):
        erros = 0
        for i in range(max_lines):
            cima = s - i - 1
            baixo = s + i
            if baixo >= max_lines or cima < 0:
                break
            for c in range(max_col):
                if lines[cima][c] != lines[baixo][c]:
                    erros += 1
        if erros == 1:
            val1 += 100 * s

print("Parte 1:", val)
print("Parte 2:", val1)

