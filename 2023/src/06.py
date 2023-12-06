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


print( time )
print(distance)

ans = 1
for i, t in enumerate(time):
    res = [ 1 for x in range(t) if (t - x) * x > distance[i] ]
    ans *= sum(res)

print(ans)


time = [ t for t in arquivo[0].split(":")[1].strip().split() ]
distance = [ d for d in arquivo[1].split(":")[1].strip().split() ]

time = int(''.join(time))
distance = int(''.join(distance))

print(time, distance)

res = [ 1 for x in range(time) if (time - x) * x > distance ]

print(sum(res))
