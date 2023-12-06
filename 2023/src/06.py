#!/usr/bin/env python3


import os
import re


test = 0
part = "1"
dia = "06"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()

time = [ int(t) for t in arquivo[0].split(":")[1].strip().split() ]
distance = [int(d) for d in arquivo[1].split(":")[1].strip().split() ]

ans = 1
for i, t in enumerate(time):
    res = [ 1 for x in range(t) if (t - x) * x > distance[i] ]
    ans *= sum(res)

time = [ t for t in arquivo[0].split(":")[1].strip().split() ]
distance = [ d for d in arquivo[1].split(":")[1].strip().split() ]

t = int(''.join(time))
d = int(''.join(distance))

x_0 = ( -t +  ( t ** 2 - 4 * d ) ** (1/2) ) / ( -2 )
x_1 = ( -t -  ( t ** 2 - 4 * d ) ** (1/2) ) / ( -2 )

x_0 = round(x_0)
x_1 = int(x_1)

print("=" * 80)
print(f'parte 1: {ans}')
print("=" * 80)
print(f'x_0: {x_0}')
print("=" * 80)
print(f'x_1: {x_1}')
print("=" * 80)
print( f'parte 2: {x_1 - x_0}' )
print("=" * 80)

#res = [ 1 for x in range(time) if (time - x) * x > distance ]

