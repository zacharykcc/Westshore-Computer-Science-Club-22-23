#!/usr/bin/env python3

import sys, binascii, hashlib

def xorByteArray(a, b):
	# This bit of cleverness from stackoverflow post
	# https://stackoverflow.com/questions/52851023/python-3-xor-bytearrays
	retVal = (bytes(x ^ y for (x,y) in zip(a,b)))
	return retVal


def main(argv):

	verifyHash = "09e88704076dc95cc91bc4fead6504090b966a042fdac36b4c03ec7796902d4e"
	ciphertext = b'16bc8366459642f9379d63f8496989e0116bc09df25fb184da8d0bd1b4ce0ee2198e53b12c73e123b285ec83125037c39e35789c526da948539a22ef2930d655'


	if (len(argv) != 2):
		print("Usage: {} romname".format(argv[0]))
		return

	romData = open(argv[1], "rb").read()
	
	hash256 = hashlib.sha256()
	hash256.update(romData)

	hash512 = hashlib.sha512()
	hash512.update(romData)

	#print("Verification Hash = {}".format(hash256.hexdigest()))
	if (verifyHash != hash256.hexdigest()):
		print("ROM verification failed")
		return

	print("ROM Verified.  Calculating flag")

	oneTimePad = hash512.digest()
	flagText = xorByteArray(oneTimePad, binascii.unhexlify(ciphertext))

	print("Flag = {}".format(flagText.decode("utf-8")))
	


if __name__ == "__main__":
	main(sys.argv)
