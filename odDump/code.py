
while True:
    octalNumber = input("OctalPOS: ")
    octalNumber = list(octalNumber)

    
    Fourth = int(octalNumber[1]) * 4096
    Third = int(octalNumber[2]) * 512
    Second = int(octalNumber[3]) * 64
    First = int(octalNumber[4]) * 8
    Zeroth = int(octalNumber[5])


    decimalVal = First+Second+Third+Fourth+Zeroth

    hexVal = str(hex(decimalVal))
    hexVal = hexVal[2:]

    letters = [str(hexVal[:2]),str(hexVal[2:4])]

    print(str((bytes.fromhex(letters[1])).decode("ASCII"))+" "+str((bytes.fromhex(letters[0])).decode("ASCII")))
