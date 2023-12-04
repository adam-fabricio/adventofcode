#!/usr/bin/env python3


import os
import re


test = 0
part = "2"
dia = "03"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

max_line = len(arquivo)
max_col = len(arquivo[0])

numbers = []
simbolos = []

for l_n, line in enumerate(arquivo):
    numbers += ([[int(n.group()), l_n, n.span()]
        for n in re.finditer("\d+", line)] )
    simbolos += [[s.group(), l_n, s.span() ] for s in re.finditer("[^\d^\.]", line)]
    print(l_n, "->", line, "<-", l_n)


ans = 0
part_2 = {}

for n_l in numbers:
    num, line, (p_i, p_f) = n_l
    valido = False
    for p in range(p_i-1, p_f+1):
        for l in range(line-1, line + 2):
            if l < 0 or l >= max_line or p < 0 or p >= max_col:
                continue
            if not arquivo[l][p].isdigit() and not arquivo[l][p] == ".":
                if arquivo[l][p] == "*":
                    if f'{l}, {p}' in part_2:
                        part_2[f"{l}, {p}"].append(num)
                    else:
                        part_2[f"{l}, {p}"] = [ num ]
                valido = True
                ans += num

                break
        if valido:
            break
print(ans)

ans_2 = 0
for k in part_2:
    if len(part_2[k]) > 1:
        ans_2 += part_2[k][0] * part_2[k][1]

print(ans_2)

# 
# for s_l in simbolos:
#     simbolo, line, (p_i, p_f) = s_l
#     if simbolo != "*":
#         continue
#     for p in range(p_i-1, p_f+1):
#         for l in range(line-1, line + 2):
#             if l < 0 or l >= max_line or p < 0 or p >= max_col:
#                 continue
#             if arquivo[l][p].isdigit():
#                 print(s_l)
# 
# 
# 
