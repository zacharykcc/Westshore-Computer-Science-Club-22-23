# Games, Housing, Dating, Hobbies, School, Groceries, Automotive, Streaming, Sports, Concerts, HomeImprovement, 
with open("chal.txt", "r") as file:
    content = file.readlines()
posistion = 1
columns = 0
rows = 0

for count in range(int(content[0])):
    matrix = [[],
              []]
    for count in range( (int(str(content[posistion])[:1]))):
        posistion += 1
        matrix.append( ((content[posistion]).split())[0] )
        columns += 1
    
    for count in range(int(str(content[posistion])[1:2]) ):
        print("filler")