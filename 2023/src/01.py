#!/usr/bin/env python3


import os
import re


test = 0
part = "2"
dia = "01"

if test:
    dia = dia + "_test"

path = os.path.join("data", dia)

num = "one, two, three, four, five, six, seven, eight, nine, 1, 2, 3, 4, 5, 6, 7, 8, 9"
num_1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

list_num = [ i.strip() for i in num.split(',') ]
str_list_num = '|'.join(list_num)

dict_num = dict(zip(list_num, num_1))

with open(path) as f:
    arquivo = f.read()
p_1 = []
lista = []
for n, linha in enumerate(arquivo.splitlines()):
    parte_1 = re.findall("(?=(\d))", linha)
    matches = re.findall(f"(?=({str_list_num}))", linha)
    p_1.append(int(parte_1[0]+parte_1[-1]))
    lista.append(int(dict_num[matches[0]] + dict_num[matches[-1]]))
print(sum(lista))
print(sum(p_1))
