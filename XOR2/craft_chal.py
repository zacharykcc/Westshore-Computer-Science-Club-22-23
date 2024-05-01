#!/usr/bin/env python3

import random

flag = open("flag.txt","r").read().strip()

key = random.randint(0,255)

outputText = ""
for curchar in flag:
	outputText += hex(ord(curchar) ^ key)
	outputText += " "
	key += 1
	key %= 0x100

print(outputText)

