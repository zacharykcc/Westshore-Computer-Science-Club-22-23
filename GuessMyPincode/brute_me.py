#!/usr/bin/env python3

import sys, binascii, hashlib

def xorByteArray(a, b):
	# This bit of cleverness from stackoverflow post
	# https://stackoverflow.com/questions/52851023/python-3-xor-bytearrays
	retVal = (bytes(x ^ y for (x,y) in zip(a,b)))
	return retVal


def main(argv):

	pinXorFlagHex = b'e2438a3eaf2e062fb19db222e432ad72d96a7241180589625349d2494d185c89'
	flagHashHex   = b'2fa10295c24c1accb124b4ddd58de6e99e69fa296a20563d46304eae709a053a'
	pinXorFlag = binascii.unhexlify(pinXorFlagHex)
	flagHash = binascii.unhexlify(flagHashHex)

	if (len(argv) != 2):
		print("Usage: {} xxxx".format(argv[0]))
		print("  Where xxxx is you 4 digit pin code")
		return

	pincode = argv[1]
	if (len(pincode) != 4):
		print("Pin code {} is not 4 digits".format(argv[1]))
		return

	pinhash = hashlib.sha256()
	pinhash.update(hex(int(pincode)).encode("utf-8"))

	flag = xorByteArray(pinhash.digest(), pinXorFlag)

	flagHashForUserPin = hashlib.sha256()
	flagHashForUserPin.update(flag)
	if (flagHashForUserPin.digest() == flagHash):
		print("Congratulations")
		print(flag.decode("utf-8"))
	else:
		print("Invalid pin")

if __name__ == "__main__":
	main(sys.argv)
