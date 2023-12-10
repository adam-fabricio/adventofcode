#!/usr/bin/env python3

import os

dia = 15
local = "assets"
part = "1"
test = 1

nome_arquivo = str(dia) if not test else str(dia) + "_test"

with open(os.path.join(local, nome_arquivo)) as arquivo:
    arquivo = arquivo.read()

print(arquivo)
