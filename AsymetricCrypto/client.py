#!/usr/bin/env python3

import os, sys, socket
import binascii
import threading

#import Crypto.cipher
from Cryptodome.Cipher import AES

def debug(msg):
	if (False):
		sys.stderr.write(msg + "\n")

# May need python3-pycryptodome, but it is likely already installed

def encryptMsg(msg, key):
	nonce = os.urandom(8)
	debug("ENC Nonce = {}".format(binascii.hexlify(nonce)))
	cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
	ct = cipher.encrypt(msg)
	return binascii.hexlify(nonce + ct) + b'\n'

def decryptMsg(hexmsg, key):
	if (len(hexmsg) < 16):
		print("Error with message, too short")
		return b""

	# Strip out any newlines
	hexmsg = hexmsg.replace(b'\n',b'')

	msg = binascii.unhexlify(hexmsg)

	nonce = msg[:8]
	ct = msg[8:]
	debug("  DECRYPT NONCE={}".format(binascii.hexlify(nonce)))
	debug("  DECRYPT CT={}".format(binascii.hexlify(ct)))

	cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
	pt = cipher.decrypt(ct)
	return pt

# Passing aesKey in list so it will be by-reference
def processIncomingMsg(aesKey, msg):
	debug("Processing msg = {} with aeskey = {}".format(msg, aesKey))

	if (len(msg) < 1):
		return

	if (len(aesKey) == 0):
		if (msg.startswith(b'AES=')):
			# This message contains the AES key
			aesKey.append(binascii.unhexlify(msg[4:]))
			print("AES key received!")
		else:
			# This is a plaintext message
			print("UNENCRYPTED TEXT: {}".format(msg.decode("utf-8")))
	else:
		incomingPt = decryptMsg(msg, aesKey[0])
		print(incomingPt.decode("utf-8"))

def main(argv):
	if (len(argv) != 3):
		print("Need to specify an address and port number")
		return

	serverAddr = argv[1]
	serverPort = int(argv[2])

	print("Welcome to WC Secret Storage Client (AES-128 protected!)")

	'''
	# AES encryption test code
	aesKey = os.urandom(128//8)

	print("AESKEY={}".format(binascii.hexlify(aesKey)))

	pt = b"Hello"
	ct = encryptMsg(pt, aesKey)
	debug("Sample CT = {}".format(ct))

	debug("Now, decrypt")

	pt2 = decryptMsg(ct, aesKey)
	debug("PT after = {}".format(pt2))
	'''

	print("Attempting to connect to {} on port {}".format(serverAddr, serverPort))
	clientSock = socket.create_connection( (serverAddr, serverPort) )

	# aesKey is an empty list, or a list of 1 item.  It's a list so we can pass the aesKey by reference
	aesKey = []

	while(True):
		incomingMessages = clientSock.recv(2000)

		if (len(incomingMessages) <= 0):
			print("Disconnected")
			break

		msgList = incomingMessages.split(b'\n')
		for msg in msgList:
			processIncomingMsg(aesKey, msg)
		
		if (aesKey):
			# Can only send outgoing messages once aes key recieved
			outMsg = sys.stdin.readline().strip()
			outCt = encryptMsg(outMsg.encode("utf-8"), aesKey[0])
			clientSock.send(outCt + b"\n")



if __name__ == "__main__":
	main(sys.argv)
