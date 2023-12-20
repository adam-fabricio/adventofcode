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
    arquivo = f.read()


