#!/usr/bin/env python3

import time, random

print("Calculating digits of pi...  please wait")

numDigits = 100
for i in range(6):
	time.sleep(random.randrange(100, 300) / 100)
	numDigits += random.randrange(50,75)
	print("Calculated {} digits of pi...  please wait!".format(numDigits))

print("Your computer to slow.")
print("wildcat{d4t4_l34k3r}")


