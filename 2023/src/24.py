#!/usr/bin/env python3


import os
import re
from sys import argv


test = 0 if len(argv) == 2 else 1
part = "1"
dia =  argv[0][-5:-3]

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

with open(path) as f:
    arquivo = f.read().splitlines()


granizos = [[float(valor) for valor in re.findall("[-]?\d+", linha)]
        for linha in arquivo]

r = [200000000000000, 400000000000000]
#r = [7, 27]
ans = 0
for a in range(len(granizos)-1):
    m_a = granizos[a][4] / granizos[a][3]
    b_a = granizos[a][1] - m_a * granizos[a][0]
    for b in range(a+1, len(granizos)):
        m_b = granizos[b][4] / granizos[b][3]
        if m_a == m_b:
            continue
        b_b = granizos[b][1] - m_b * granizos[b][0]
        x = (b_b - b_a) / (m_a - m_b)
        y = x * m_a + b_a
        t_a = (x - granizos[a][0]) / granizos[a][3]
        t_b = (x - granizos[b][0]) / granizos[b][3]
        #input(f"{x}, {y}, {t_a}, {t_b}")

        if t_a <= 0 or t_b <= 0 or not r[0] < x < r[1] or not r[0] < y < r[1]:
            continue
        
        ans += 1

print(ans)

ans = []
coeficientes = []
for i in range(4):
    """
    Equações da reta:
    reta 1:
        x = vx1 * t + x1
        y = vy1 * t + y1
        z = vz1 * t + z1
    reta : Reta que precisamos calcular
        x = VX * t + X
        y = VY * t + y
        z = VZ * t + z

    Sistema de equaçoes ponto comum (x, y, z iguais em duas retas)
    reta 1 
        x = vx1 * T1 + x1 = VX * T1 + X
        y = vy1 * T1 + y1 = VY * T1 + y
        z = vz1 * T1 + z1 = VZ * T1 + z
    SISTEMA
    T1 * ( VX - vx1 ) = x1 - X
    T1 * ( VY - vy1 ) = y1 - Y

    T1 = ( x1 - X ) / ( VX - vx1 )
    T1 = ( y1 - Y ) / ( VY - vy1 )

    T1 = ( x1 - X ) / ( VX - vx1 ) = ( y1 - Y ) / ( VY - vy1 )

    (x1 - X) * (VY -vy1) = (y1 - Y) * (VX -vx1)

    VY*x1 - x1*vy1 - X*VY + vy1*X = VX*y1 - vx1*y1 - Y*VX + Y*vy1

    Y*VX - X*VY =  x1*vy1 -VY*x1 - vy1*X + VX*y1 - vx1*y1 + Y*vx1

    analogo para reta 2 teremos

    Y*VX - X*VY =  x2*vy2 -VY*x2 - vy2*X + VX*y2 - vx2*y2 - Y*vx2

    juntando reta 1 e 2 teremos

    x1*vy1 - VY*x1 - vy1*X + VX*y1 - vx1*y1 - Y+vx1 = \
    x2*vy2 - VY*x2 - vy2*X + VX*y2 - vx2*y2 + Y*vx2

    organizando em X, Y, VX, Z teremos:

    (vy2 - vy1) * X + (vy1 - vy2) * Y + (y1 - y2) * VX + (x2 - x1) * VY = \
            y1*vx1 - x1*vy1 + x2*vy2 - y2*vx2

    Como temos 4 variaveis X, Y, VX, VZ:

    Com 4 retas teremos 4 equacoes: 1 - 2, 1-3 e 1-4
    """
    x1, y1, z1, vx1, vy1, vz1 = granizos[i]
    x2, y2, z2, vx2, vy2, vz2 = granizos[i+1]

    x = vy2 - x1
    y = vy1 - vy2
    vx = y1 - y2
    vy = x2 -x1
    coeficiente_linear = y1 * vx1 - x1 * vy1 + x2*vy2 - y2 * vx2

    coeficientes.append([x, y, vx, vy, coeficiente_linear])

print(coeficientes)

for i in range(len(coeficientes)):
    pivo = coeficientes[i][i]:
        for j in range(len(coeficientes)):
            coeficientes[i][ = oceficientes[i][j]
