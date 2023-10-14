key = "8c06d6fce2dddb70e8e5ef893ef9a569"

import os, sys, socket
import binascii
import threading

from Cryptodome.Cipher import AES




	


AesKey = binascii.unhexlify(key)





def debug(msg):
	if (False):
		sys.stderr.write(msg + "\n")



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

def encryptMsg(msg, key):
	nonce = os.urandom(8)
	debug("ENC Nonce = {}".format(binascii.hexlify(nonce)))
	cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
	ct = cipher.encrypt(msg)
	return binascii.hexlify(nonce + ct) + b'\n'

#print(decryptMsg("", key))

print(decryptMsg(b"d9aafc4713ad0f893b618ae880", AesKey))
print(decryptMsg(b"a7baee237a9c6471cda9c062602c891222", AesKey))
print(decryptMsg(b"1a18da24b5f394cfb1bbffa56f0b5105806da55b79643305b052662cf72bf8", AesKey))
print(decryptMsg(b"e318095b56aaee92e774e1060ae1dfb6dfdf10bb9c383eeb", AesKey))
print(decryptMsg(b"4a71eb8cb5ca66a7f6daf1c45941866075", AesKey))
print(decryptMsg(b"be5bbdb34768973ad93e9a2267d3e4", AesKey))
print(decryptMsg(b"bc6b3865aba48d18c1b84b5dd29b275dda", AesKey))
print(decryptMsg(b"b5a73b85966e08dc53fe6d28ed667fdd", AesKey))
print(decryptMsg(b"d7e6cf1e374a795215a3766ea71b1e515fd22240ccc54caf", AesKey))
print(decryptMsg(b"e8c1990a42c4836135df9ab2e444525d61", AesKey))
print(decryptMsg(b"ad1b855bd7a0fa72bbc29551acafd4773d03312cc40bfa82", AesKey))
print(decryptMsg(b"53da278a8f81dc2228a22084bca2c0633a", AesKey))
print(decryptMsg(b"a0120cf45270a6baa5250c3921906346e9", AesKey))
print(decryptMsg(b"e569cc4493b4ca6aa35520727488071c65", AesKey))
print(decryptMsg(b"a7ba891f77c6ff0d11793ba15a81c096b720f581a1", AesKey))
print(decryptMsg(b"2b6e87dcaf752bdadcaf9451a3039aa42c", AesKey))
print(decryptMsg(b"73da7ac131b6e11271bad2ac450929da49acc5e12992988e", AesKey))
print(decryptMsg(b"d92e138ea880ad0ad99b444a0d52010740", AesKey))
print(decryptMsg(b"b99d2e9bb68d1208173d506cfdaf92dc5081887f22", AesKey))
print(decryptMsg(b"7b425211da05800c196eafe5c51e1e6ea8", AesKey))
print(decryptMsg(b"60ea4eeb2d71e2153224bcd1e325bcd3e33f1b65d4abef75ea711cc7c1783db70a3d4768", AesKey))
print(decryptMsg(b"09216a48d7f9ddd788452c22731b68181bb297870713bd7656307b3246c00a6a57f67c017d38fbd9001662a8442a4cd00e549f7a42074518aa642f813c8c2ca0478f2095a2d6a9d26415c0c7c7328bc6b4a921209912dd61bea81a9a668cb27730f525c8e8fb215db5ab09b3edb4cade1ff5e1d4cc2a29862a08371071834e783b5d3545490412b59a42c2c0e6dc0e102d875f14180598cacb1ac1d1d7f95106796be8ab3c2cb1afce76f811bc4dbfb18613300b8f70cc54a4a00572b1476a0c1dc0049282266ea6b1effce8b9bbc01709f0c4a860908e1f5e6c1155bea01f9972f7397eadd1fcf9df2ea3f8497abbca1fe1834e683fca456ce9ec850f29474a098afe98a73d0371c1025679a7d54a7c9f30e732ce4212345d088ebf08100c16537137b662cbef14", AesKey))
print(decryptMsg(b"9a39ea5163a22ca1de620cdb1cea6359b4", AesKey))
print(decryptMsg(b"c12a6e898ff576c5fa95b8f14503c5c072846712", AesKey))