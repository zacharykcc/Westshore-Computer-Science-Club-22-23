#!/usr/bin/env python3

import sys, hashlib, binascii

VERIFY_HASH = b"d093ebbe903066b10665440ab80a29fa97af6d8c56641300b374e75e71c5d21d"
CIPHER_HASH = b"d54ca8848f937966cc447944e031e9f113b3a26037face62236f0f0c929b5d88d5d09c51cdd67b3dc5b66e0e45e77623a8072755920662078ac8f5d60b221455"

def debug(msg):
	if(False):
		sys.stderr.write(msg + "\n")

def cleanLineEndings(text):
	cleanOutput = ""
	textLines = text.split("\n")
	for singleLine in textLines:
		cleanOutput += singleLine.strip()
		cleanOutput += "\n"
	cleanOutput.strip()
	return cleanOutput

def createHashes(text):
	verifyHash = hashlib.sha256()
	verifyHash.update(text.encode("utf-8"))

	keyHash = hashlib.sha512()
	keyHash.update(text.encode("utf-8"))

	return (verifyHash.digest(), keyHash.digest())

def xorByteArray(a, b):
	# This bit of cleverness from stackoverflow post
	# https://stackoverflow.com/questions/52851023/python-3-xor-bytearrays
	retVal = (bytes(x ^ y for (x,y) in zip(a,b)))
	return retVal

def main(args):
	rawOutput = sys.stdin.read().strip()

	cleanOutput = cleanLineEndings(rawOutput)
	
	verifyHash, keyHash = createHashes(cleanOutput)

	debug("Verify Hash  = {}".format(binascii.hexlify(verifyHash)))
	debug("Key Hash     = {}".format(binascii.hexlify(keyHash)))
	debug("Key Hash Len = {}".format(len(keyHash)))
	debug("CipherText   = {}".format(CIPHER_HASH))

	if (VERIFY_HASH != binascii.hexlify(verifyHash)):
		print("Output incorrect")
		return

	# Encrypt the flag
	plainText = xorByteArray(keyHash, binascii.unhexlify(CIPHER_HASH))
	debug("Plaintext    = {}".format(binascii.hexlify(plainText)))

	print("Congrats!")
	print(plainText.decode("utf-8"))

if __name__ == "__main__":
	main(sys.argv)

