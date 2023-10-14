#!/usr/bin/env python3

flag = open("chal.txt","r").read().strip()

outputText = ""
for curchar in flag:
	outputText += hex(ord(curchar) ^ 0x83)
	outputText += " "

print(outputText)


