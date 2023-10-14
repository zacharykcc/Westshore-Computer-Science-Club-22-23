#!/usr/bin/env -S python3 -u
# -S lets you pass python3 args, -u is to have output unbuffered

import random, sys

def readRandomLineFromFile(filename):
	try:
		f = open(filename,"r")
		fileText = f.read()
		linesOfFile = fileText.split("\n")
		return random.choice(linesOfFile)
	except:
		retVal = "If you were playing online, you would get a random line\n"
		retVal += "from the file {}".format(filename)
		return retVal

def readEntireFile(filename):
	#print("displayFile({})".format(filename))
	try:
		f = open(filename,"r")
		fileText = f.read()
		return fileText
	except:
		retVal = "If you were playing online, you would see all the text\n"
		retVal += "from the file {}".format(filename)
		return retVal

def commonCommands(itemList, cmd):
	if (cmd == "exit"):
		print("Thanks for playing!")
		sys.exit(0)
		# Doesn't return
	elif (cmd == "inventory"):
		print("  Inventory:")
		for curItem in itemList:
			print("  " + curItem)
		return True
	elif (cmd == "print flag"):
		if ( ("start of flag" in itemList) and ("middle of flag" in itemList) and ("end of flag" in itemList) ):
			print("Congrats on finding all parts of the flag:")
			print(readEntireFile("flag.txt"))
		else:
			print("You don't have all 3 parts of the flag")
	return False
			

def openField(itemList):
	print("Wildcat Adventure: The CTF (Demo Version - 5 minute playtime)")
	print("Copyright 2023, Licensed under the GPL")
	print("Wildcat Adventure is not a registered trademwark")
	print("Revision 01 / Serial {}".format(random.randint(100, 9999)))
	print("")

	while(True):
		print("")
		print("West of House")
		print("You are standing in an open field west of a white house, with a boarded front")
		print("door.  There is a small mailbox here.  To the south is a road.")
		print("")
		print("Hint: Try the 'look' command")
		print("> ",end="")

		cmd = sys.stdin.readline().strip()

		if (commonCommands(itemList, cmd)):
			continue
		elif (cmd == "look"):
			print(readEntireFile("zork.txt"))
		elif ( (cmd == "goto house") or (cmd == "east") ):
			inHouse(itemList)
		elif (cmd == "west"):
			print("You walk directly into some bushes.  You wonder what the heck you are doing")
			print("You are 'West of House', you should try walking east to goto the house")
		elif (cmd == "south"):
			onRoad(itemList)
		else:
			print("Invalid command {}.  Have you tried the 'look' command?".format(cmd))

def onRoad(itemList):
	while(True):
		print("")
		print("The street sign for the road says Crist Dr.  There are a bunch of houses farther down the")
		print("street, but you are feeling lazy, and there is no way you are willing to walk any farther")
		print("down this dumb road.  There is an open field to the north.  There is a phone booth by the")
		print("street sign.  There is a house that says 'Jobs Family' on the mailbox")
		print("> ",end="")
		
		cmd = sys.stdin.readline().strip()

		if (commonCommands(itemList, cmd)):
			continue
		elif(cmd == "enter phonebooth"):
			inPhoneBooth(itemList)
		elif(cmd == "goto house"):
			jobsHouse(itemList)
		elif(cmd == "north"):
			# goback to the open field
			return
	
def inPhoneBooth(itemList):
	while(True):
		print("")
		print("You are in a phone booth.  The phone has a quarter slot to pay for phone calls, and the phone looks operational")
		print("There is a phone book where you can look up the phone number for a person in the local town")
		print("> ", end="")
		
		cmd = sys.stdin.readline().strip()

		if (commonCommands(itemList, cmd)):
			continue
		elif(cmd == "call steve jobs"):
			if ("whistle" in itemList):
				callJobs(itemList)
			else:
				print("You looks up the phone number in the book, and dial it with the phone, but a recording says that you need")
				print("to put a quarter in the phone to continue the phone call")
		elif(cmd == "call woz"):
			if ("whistle" in itemList):
				callWoz(itemList)
			else:
				print("You looks up the phone number in the book, and dial it with the phone, but a recording says that you need")
				print("to put a quarter in the phone to continue the phone call")
		elif(cmd == "exit phonebooth"):
			print("You leave the phone booth and go back to the street")
			return
		elif(cmd == "call 911"):
			print("You pick up the handset and dial 911.  The 911 operator quickly answers and asks you what your emergancy is?")
			print("You don't have anything to say and just make some grunting noises, and then hang up.  Before you have a chance")
			print("to react you notice that a police car with lights and sirens has turned onto the road and is now heading in")
			print("your direction.  The officer pulls up, orders you out of the phone booth.  You are so shocked that you are")
			print("slow to respond.  You get tazed.  The officer arrests you and you goto jail. Game Over.")
			sys.exit(0)


def jobsHouse(itemList):
	while(True):
		print("")
		print("As you approach the house you hear a couple of people in the garage working on something, but the garage door is")
		print("shut, and you can't see in.  You knock on the door door no one answers.  Maybe you should try calling them...")
		print("You see the road behind you")
		print("> ", end="")

		cmd = sys.stdin.readline().strip()

		if (commonCommands(itemList, cmd)):
			continue
		elif(cmd == "road"):
			print("You walk back to the road")
			return

def callJobs(itemList):
	print(readEntireFile("apple.ansi"))
	print(readEntireFile("jobs.txt"))
	itemList.append("end of flag")

def callWoz(itemList):
	print(readEntireFile("whistle.txt"))
	print("")
	print(readRandomLineFromFile("woz.txt"))
	
def inHouse(itemList):
	while(True):
		print("")
		print("As you walk up to the house you notice a sign hanging from it that says 'Lightman Residence'.  You knock on the front")
		print("door when you get there, and a young man opens the door.  He introduces himself as David.  You tell me that you are")
		print("working on a cybersecurity computer challenge, and you can immediately see the excitement on David's face.  He tells")
		print("you that he also is into computers, and invites you to come into his house.  You walk in and see his computer sitting")
		print("on a desk in the main room.  It looks like his computer is connected to a phone.")

		if ("whistle" not in itemList):
			print("There is a cheap plastic whistle on the ground.")

		print("> ", end="")

		cmd = sys.stdin.readline().strip()

		if (commonCommands(itemList, cmd)):
			continue
		elif(cmd == "exit house"):
			print("You wave goodbye and tell David you need to go 'hack the planet'.  David looks at you confused, and says wrong")
			print("movie bro, I'm from War Games, not Hackers")
			return
		elif( (cmd == "pick up whistle") and ("whistle" not in itemList) ):
			print("You bend over and pick up the plastic whistle.  It feels really cheap.  It says Captain Crunch on it")
			itemList.append("whistle")
		elif( cmd == "use computer"):
			useComputer(itemList)

def useComputer(itemList):
	while(True):
		print("")
		print("You set down at David's computer.  It't got an old CRT monitor with green text.  David fires up his modem program")
		print("and dials up a new server he found for a computer games company that he found war dialing the other day.  He made")
		print("a program that just dialed 10,000 phone numbers for the phone prefix that is commonly used in his town.  The system")
		print("he dials just presents a simple prompt that says 'Login:'.  What should we type?")


		print("> ", end="")

		cmd = sys.stdin.readline().strip()

		if (commonCommands(itemList, cmd)):
			continue
		elif(cmd == "type joshua"):
			loginWopr(itemList)
		elif(cmd == "get up from computer"):
			print("You tell David that you'll let him take over now and get up from the computer")
			return

def loginWopr(itemList):
	while(True):
		print("")
		print("After you login with the word Joshua, you expect a password prompt, but none is needed.  The admins of this system")
		print("must not be really concerned about security. The screen flashes a few times and then says 'Greetings Progessor")
		print("Falken.  Would you like to play a game?  It then lists some games including tic-tac-toe, chess, guess a number,")
		print(", and global thermonuclear war")
	
		print("> ", end="")

		cmd = sys.stdin.readline().strip()

		if (commonCommands(itemList, cmd)):
			continue
		elif(cmd == "chess"):
			print("When you tell the system that you want to play a game of chess. The system starts rambling about Department of")
			print("Defense budgets, something called the WOPR, and government funding shortfalls, and ultimately decides that the")
			print("game of chess hasn't actually been implemented.  And perhaps you should try a different game")
		elif(cmd == "tic-tac-toe"):
			print(readEntireFile("tictactoe.ansi"))
			print("After telling the system that you want to play Tic-Tac-Toe, it quickly draws a giant full screen Tic-Tac-Toe")
			print("board on the screen and then picks it's square.  You play back and forth with it, but the game ends in a draw")
			print("You play several more games, all the games ending with ties.  This seems boring")
		elif(cmd == "guess a number game"):
			playGuessANumberGame(itemList)
		elif(cmd == "logout of server"):
			print("You logout of the session")
			return
		elif(cmd == "global thermonuclear war"):
			print(readEntireFile("wopr.ansi"))
			print(readEntireFile("wopr.txt"))
			itemList.append("start of flag")

def playGuessANumberGame(itemList):
	numberToGuess = random.randint(1,100)
	while( (numberToGuess % 16 < 10) and ((numberToGuess & 0xf) < 10) ):
		numberToGuess = random.randint(1,100)

	while(True):
		print("")
		print("The computer tells you that you that it is thinking of a number between 1 and 100")
		print("> ", end="")
		
		try:
			number = int(sys.stdin.readline(), 16)
		except:
			print("You have to enter a number!")
			continue

		if (number > numberToGuess):
			print("Too high")
		elif (number < numberToGuess):
			print("Too low")
		else:
			print("Good guess!")
			print(readEntireFile("joshua.txt"))
			itemList.append("middle of flag")
			return
			
def main():
	openField([])







if __name__ == "__main__":
	main()


# east
# use computer
# type joshua
# guess a number game



# pick up whistle
# exit house
# enter phonebooth
# call steve jobs
		# 3rd part of flag "cant_swim}"




#call woz
	# dont use "beef stew" its not strganoff



#wildcat{   help_i_cant_swim}