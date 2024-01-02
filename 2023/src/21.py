#!/usr/bin/env python3


import os
import re
from collections import deque
from sys import argv


#-----------------------------------------------------------------------------#
def p_m():
    print("-" * 20, i, len(marked), "-" * 20, sep='  ' )
    for l in range(l_max):
        for c in range(c_max):
            if (l, c) in marked:
                print("O", end='')
            else:
                print(grid[l][c], end='')
        print()
#-----------------------------------------------------------------------------#


test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

print("--- Day 21: Step Counter ---")
#-----------------------------------------------------------------------------#
grid = [ [c if not c == "S" else "."  for c in line ] for line in arquivo ]
start = [ (l, c) for l, line in enumerate(arquivo)
        for c, col in enumerate(line) if col == "S"][0]
l_max = len(arquivo)
c_max = len(arquivo[0])
direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
marked = set()
fila = deque()
n_fila = deque()
#-----------------------------------------------------------------------------#
#  n_fila.append(start)
#  marked.add(start)
#  
#  for i in range(6):
#      fila = n_fila
#      n_fila = deque()
#      while fila:
#          pos_l, pos_c = fila.popleft()
#          marked.discard((pos_l, pos_c))
#          for l, c in direcoes:
#              n_pos_l, n_pos_c = pos_l+l, pos_c+c
#              if grid[n_pos_l][n_pos_c] == ".":
#                  if (n_pos_l, n_pos_c) not in marked:
#                      marked.add((n_pos_l, n_pos_c))
#                      n_fila.append((n_pos_l, n_pos_c))
#  
#  print("Parte 1:", len(marked))
#-----------------------------------------------------------------------------#
start = int((l_max - 1) / 2), int((c_max - 1) / 2)
direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
marked = set()
fila = deque()
n_fila = deque()

#-----------------------------------------------------------------------------#
n_fila.append((start, (0, 0)))

ans = []
impar = 0
par = 0
for i in range(l_max*3):
    fila = n_fila
    n_fila = deque()
    while fila:
        (pos_l, pos_c), (map_l, map_c) = fila.popleft()
        for l, c in direcoes:
            n_pos_l, n_pos_c = pos_l+l, pos_c+c
            n_map_l, n_map_c = map_l, map_c
            if n_pos_l < 0:
                n_pos_l = l_max - 1
                n_map_l -= 1

            elif n_pos_l == l_max:
                n_pos_l = 0
                n_map_l += 1

            elif n_pos_c < 0:
                n_pos_c = c_max - 1
                n_map_c -= 1

            elif n_pos_c == c_max:
                n_pos_c = 0
                n_map_c += 1

            if grid[n_pos_l][n_pos_c] == ".":
                if ((n_pos_l, n_pos_c), (n_map_l, n_map_c)) not in marked:
                    marked.add(((n_pos_l, n_pos_c), (n_map_l, n_map_c)))
                    n_fila.append(((n_pos_l, n_pos_c), (n_map_l, n_map_c)))
                    if i % 2 == 1:
                        impar+=1
                    else:
                        par+=1
    if i % 2 == 1:
        ans.append(impar)
    else:
        ans.append(par)


ans1 = []
for i in range(len(ans)):
    if i % l_max == 64:
        ans1.append(ans[i])
d_ans1 = []
for i in range(len(ans1)-1):
    d_ans1.append(ans1[i+1] - ans1[i])
dd_ans1 = d_ans1[1]-d_ans1[0]
a = dd_ans1 // 2
b = ans1[1] - ans1[0] - 3*a
c = ans1[1] - 4*a - 2* b
passos = 26501365
n = passos // l_max + 1
res = a*n**2 + b*n + c
print("Parte 1:", ans[63])
print("Parte 2:", res)

