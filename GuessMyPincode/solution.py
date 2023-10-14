#!/usr/bin/env python3

import time, sys, os

for count in range(1000,9999):
    brute_me = os.popen("./brute_force" + count)
    brute_me_output = brute_me.read()
    print(brute_me_output)