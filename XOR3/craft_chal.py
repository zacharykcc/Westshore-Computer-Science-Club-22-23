#!/usr/bin/env python3

import random

flag = open("flag.txt","r").read().strip()

key = random.randint(0,255)

oddkey = key
evenkey = key

if ( (len(flag) % 2) == 1):
	flag += " "

outputText = ""
for i in range(0, len(flag), 2):
	outputText += hex(ord(flag[i]) ^ evenkey)
	outputText += " "
	outputText += hex(ord(flag[i+1]) ^ oddkey)
	outputText += " "

	oddkey -= 1
	if (oddkey == -1):
		oddkey = 255
	
	evenkey += 1
	if (evenkey == 256):
		evenkey = 0

print(outputText)

