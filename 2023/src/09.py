#!/usr/bin/env python3


import os
import re


test = 0
part = "1"
dia = "09"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()


reports = [ [ int(v) for v in l.split(" ") ] for l in arquivo ]

ans1=0
ans2=0

for r in reports:
    report = [ r ]
    i = 0
    while not all( elemento == 0 for elemento in report[i] ):
        report.append( [ report[i][el+1] - report[i][el] for el
                        in range(len(report[i]) - 1 )] )
        i += 1
    for i in range(len(report) - 2, -1, -1):

        report[i].append( report[i][-1] + report[i+1][-1] )

        report[i].insert(0, report[i][0] - report[i+1][0] )

    ans1 += report[0][-1]
    ans2 += report[0][0]

print("parte 1:", ans1)

print("parte 2:", ans2)
