#!/usr/bin/env -S python3 -u

import hashlib, gzip, base64, sys, os.path, binascii, time

def debug(msg):
	if(False):
		sys.stderr.write(msg + "\n")

#******************************************************************************
# Don't worry about any of this stuff BELOW, it won't help you
#******************************************************************************

POKEMON_NAMES_ENC = '''
	H4sIAAAAAAAAA01Uy3LcOAy84yty29v+g+2xx2vH66koNanKDZIwEksUqYCkZc3Xp0FNtvaiblIQ
	ng3dF99y4qL0z8dW8SyhVPIwss4cerlR8RJDpe7K2lPzqzjNXugHa46V3XtOObok9MBZdHFCb5J5
	iT3dl4ybiwrsRXoYv/JUAtM9Tuq8p5PrB9l2iDnHP4y+ceac2dB18EvNIqxxpacdHicOie60jRO+
	mbgbC2ydQYP806iy7gzpjfSv66Ny+HKRmZFGPTokYuRXEQn/Wfz/faxkcmGgBy8XdrrtpIXNufjF
	fcIioFrnE724YfDbUi4X+lFpNvqztJzpGL3Be987ZHP0Mc50dl4WX2ahEyun/SldtmnEwDvOMY90
	cIOXnOlQhqwuor9xxfVJNDkOdEpbX7rJglR84zBZU9XNwovQEQ3zDh/caccuIGE6Re9WHiqm1anf
	b5TNqlXGoHo2vPM88ZVnOO3GuOwwSUWeF0zS+7RoLNlGvLjQ4gKldRlTr/y7hMxdjH+YFvF0lNiX
	3lLjDxhBbkheZmQRtjr1xfU2t8bHdbF4RlpF6TwEmV2WnWWo84n1Irkb/+rpAK/RntalRhDoIOsQ
	Mb+jNUPprUzUjIhYFe7jlrLFHiFhv9Ezl1DPEgZWeg+Y7wHNu0LAz9sCPbwqt+1Gr5CEJX2OHlvQ
	0qPH3DSioMdPGYau5BsreE0PpY3BEoYrnujZ5TkGbz4rQyMDfXXdxLkg09d4uZji0M6r4bdxG6MG
	w37fxZAw3e8cBvE2KOSaJvPxHDUJo27uMTlTgwkbx6rgJrNupcJsO6p/v6El1HRbHlHKiwuftzq4
	Lder9XdGE04uJKcIVzQmu8Sy6ULHDWrtcfOVFxPvwdn2PsoHyjpj+dX+Gy9oj+GT53o+Rd0wDXrH
	L2ZDi4AJ6aCGFo26wYK1FvSSu7x5akJUz5+QLv4DBRP4yUu2ROBaBXEhWUjaEJ6xoTdWFSJrXm1b
	VvoNMWtZRvMEAAA='''

gPokemonNameMap = {}
gPokemonPictures = {}

def loadPokemonNames():
	rawList = gzip.decompress(base64.b64decode(POKEMON_NAMES_ENC)).decode("utf-8").split("\n")
	i = 1
	for pokemon in rawList:
		gPokemonNameMap[i] = pokemon
		i += 1

def getPokemonName(pokemonNum):
	if (len(gPokemonNameMap) == 0):
		debug("Loading Pokemon names")
		loadPokemonNames()

	if ( (pokemonNum < 0) or (pokemonNum > 151) ):
		return "InvalidPokemonNumber"

	return gPokemonNameMap[pokemonNum]

def loadPokemonPictures():
	pokedexPics = "pokedex.gz"
	if os.path.exists(pokedexPics):
		gzipFile = open(pokedexPics,"rb")
		gzipData = gzipFile.read()
		gzipFile.close()

		debug("Loaded {} bytes from gzip file".format(len(gzipData)))

		b64BinData = gzip.decompress(gzipData)
		b64Data = b64BinData.decode("utf-8").strip().split("\n")

		debug("Found {} pokedex strings".format(len(b64Data)))

		i = 1
		for bd in b64Data:
			debug("Adding pokemon {} picture".format(i))
			gPokemonPictures[i] = base64.b64decode(bd).decode("utf-8")
			i += 1
	else:
		for i in range(1, 152):
			gPokemonPictures[i] = "[Picture of {}]".format(getPokemonName(i))

def getPokemonPicture(pokemonNum):
	if (len(gPokemonPictures) < 151):
		debug("Loading Pokemon picture data")
		loadPokemonPictures()
	
	if ( (pokemonNum < 0) or (pokemonNum > 151) ):
		return "InvalidPokemonNumber"

	return gPokemonPictures[pokemonNum]

def xorByteArray(a, b):
	# This bit of cleverness from stackoverflow post
	# https://stackoverflow.com/questions/52851023/python-3-xor-bytearrays
	retVal = (bytes(x ^ y for (x,y) in zip(a,b)))
	return retVal
	
def judgeSolution(userData):
	VERIFY_HASH = "70960b64978b95c553d826e8e74a63ad5048a21e263c3d107285fdc442e9e7d9"
	FLAG_CT = "9f36b56b58b08174cda1a835ab45ff47e01fe73c3e421e03c2b3c25d12e34609b7657fa664d41250690cad47e43fa862a58ff27b75ddfd4a545ae802f4de2b71"
	
	verifyHash = hashlib.sha256()
	verifyHash.update(userData)
	
	debug("user verify hash = {}".format(verifyHash.hexdigest()))

	if (verifyHash.hexdigest() == VERIFY_HASH):
		keyHash = hashlib.sha512()
		keyHash.update(userData)
		debug("key val = {}".format(keyHash.hexdigest()))

		flagBin = xorByteArray(keyHash.digest(), binascii.unhexlify(FLAG_CT))
		debug("flagBin = {}".format(flagBin))

		print("Congrats")
		print(flagBin.decode("utf-8"))

#******************************************************************************
# Don't worry about any of this stuff ABOVE, it won't help you
#******************************************************************************


gPseudoRandomState = "zero"

def seedPrng(seedData):
	global gPseudoRandomState
	debug("PRNG state = {}".format(gPseudoRandomState))
	debug("Seeding PRNG with {}".format(seedData))

	seedSum = 0
	for singleChar in seedData:
		seedSum += ord(singleChar)

	gPseudoRandomState = str(seedSum % 12)

	debug("PRNG state = {}".format(gPseudoRandomState))

def getRandomNumber(maxVal):
	global gPseudoRandomState
	debug("PRNG state = {}".format(gPseudoRandomState))
	# Super special crytographic random number generation system
	nextStateHash = hashlib.sha256()
	nextStateHash.update(gPseudoRandomState.encode("utf-8"))
	seedHexStr = nextStateHash.hexdigest()
	
	randomVal = int(seedHexStr[-8:],16)
	
	# update state
	gPseudoRandomState = hex(randomVal)

	return (randomVal % maxVal)

def main():
	sys.stdout.write("Enter a name for your character\n")
	userName = sys.stdin.readline().strip()

	seedPrng(userName)

	randPokemonNum = getRandomNumber(151) + 1
	print("You start with {} pokemon:\n{}".format(getPokemonName(randPokemonNum), getPokemonPicture(randPokemonNum)))

	cumulativeDamage = 0
	for i in range(5):
		print("Calculating damage for hit #{}".format(i+1))
		time.sleep(1)
		damageVal = getRandomNumber(300)
		print("Damage: {}".format(damageVal))
		cumulativeDamage += damageVal

	print("Your pokemon did a cumulative damage of {}".format(cumulativeDamage))

	# If your solution is the maximum damage, this function will print the flag for you
	judgeSolution(hex(cumulativeDamage).encode("utf-8"))

if (__name__ == "__main__"):
	main()
