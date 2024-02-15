posistion = 1

with open("chal.txt", "r") as file:
    content = file.readlines()




for count in range(1000):
    if (int(content[posistion]) % 3 == 0) and (int(content[posistion]) % 7 == 0):
        print("LOCKHEEDMARTIN")
    elif int(content[posistion]) % 3 == 0:
        print("LOCKHEED")
    elif int(content[posistion]) % 7 == 0:
        print("MARTIN")
    else:
        print(int(content[posistion]))
    posistion = posistion + 1
