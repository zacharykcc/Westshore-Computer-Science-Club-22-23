#!/usr/bin/env python3

import os, sys, socket
import binascii
import threading

#import Crypto.cipher
from Cryptodome.Cipher import AES

def debug(msg):
	sys.stderr.write(msg + "\n")

# May need python3-pycryptodome, but it is likely already installed

def encryptMsg(msg, key):
	debug("  ENCRYPT: {}".format(msg))
	nonce = os.urandom(8)
	debug("ENC Nonce = {}".format(binascii.hexlify(nonce)))
	cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
	ct = cipher.encrypt(msg)
	return binascii.hexlify(nonce + ct) + b"\n"

def decryptMsg(hexmsg, key):
	if (len(hexmsg) < 16):
		print("Error with message, too short")
		return b""

	debug("  DECRYPT: {}".format(hexmsg))
	
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

def authClient(username, password):
	secretStore = open("secrets.txt", "r")
	actualUser = secretStore.readline().strip()
	actualPass = secretStore.readline().strip()
	secrets = secretStore.read()
	secretStore.close()

	print("Does {} match actual user {}".format(username, actualUser))

	if (username.decode("utf-8") != actualUser):
		return b"Invalid Username"

	print("Does {} match actual pass {}".format(password, actualPass))

	if (password.decode("utf-8") != actualPass):
		return b"Invalid Password"

	# auth success
	return secrets.encode("utf-8")


def clientHandlerThread(cs, clientPort):
	print("Thread for handling data from {} and {}".format(cs, clientPort))

	aesKey = os.urandom(128//8)
	print("Client {} will use AES key {}".format(clientPort, binascii.hexlify(aesKey)))

	cs.send(b"Welcome to WC Secret Storage Server\n")
	cs.send(b"AES=" + binascii.hexlify(aesKey) + b"\n" + encryptMsg(b"username:", aesKey) + b"\n")

	username = ""
	while(username == ""):
		#cs.send(encryptMsg(b"username:", aesKey))
		userCt = cs.recv(2000)
		if (userCt == b''):
			print("Client {} quit without ever giving us username".format(clientPort))
			return
		user = decryptMsg(userCt, aesKey)
		print("user = {}".format(user))

		cs.send(encryptMsg(b"password:", aesKey) + b"\n")
		passCt = cs.recv(2000)
		if (passCt == b''):
			print("User {} didn't give a pass, and quit".format(user))
			return
		password = decryptMsg(passCt, aesKey)

		resp = authClient(user, password)
		print("Seding response {}".format(resp))
		cs.send(encryptMsg(resp, aesKey) + b"\n" + encryptMsg(b"username:", aesKey) + b"\n")
		



	while(True):

		
		incomingMsg = cs.recv(2000)
		print("Incoming from {} = {}".format(clientPort, incomingMsg))

		if (incomingMsg == b''):
			# No more data
			print("Client {} disconnected".format(clientPort))
			return
	

def main(argv):
	if (len(argv) != 2):
		print("Need to specify a port number")
		return

	listenPort = int(argv[1])

	print("Welcome to WC Secret Storage (AES-128 protected!)")

	'''
	# AES test code
	aesKey = os.urandom(128//8)

	print("AESKEY={}".format(binascii.hexlify(aesKey)))

	pt = b"Hello"
	ct = encryptMsg(pt, aesKey)
	debug("Sample CT = {}".format(ct))

	debug("Now, decrypt")

	pt2 = decryptMsg(ct, aesKey)
	debug("PT after = {}".format(pt2))
	'''

	print("Starting a socket listener on {}".format(listenPort))
	servSock = socket.create_server( ("",listenPort), family=socket.AF_INET, reuse_port=True)
	#servSock.bind( ("", listenPort) )
	servSock.listen(5)

	while(True):
		(clientSock, addr) = servSock.accept()
		print("Received connection from {} and {}".format(clientSock, addr))

		t = threading.Thread(target=clientHandlerThread, args=( clientSock,addr) )
		t.start()
		#start_new_thread( clientHandlerThread, (clientSock, addr) )

if __name__ == "__main__":
	main(sys.argv)
