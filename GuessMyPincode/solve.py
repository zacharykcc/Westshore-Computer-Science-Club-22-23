#!/usr/bin/env python3

import os

for count in range(1000,9999):
    bruteme = os.popen("python3 brute_me.py "+str(count))
    brutemeOut = bruteme.read()
    print(brutemeOut,end="")
    print(count)
