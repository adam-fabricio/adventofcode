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


