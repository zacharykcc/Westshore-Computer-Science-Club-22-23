with open("chal.txt", "r") as file:
    content = file.readlines()

posistion = 1
columns = 0
rows = 0
tempList = []
matrixPos = 0
'''
print(content)
print(posistion)
print((str(content[posistion])[:1]))
'''



for count in range(int(content[0])):
    
    matrix = [[],
              []]
    for count in range( (int(str(content[posistion])[:1]))):
        posistion += 1
        tempList.append( ((content[posistion]).split())[0] )
        columns += 1
    matrix[0].append(tempList) 
    tempList =[]

    for count in range( (int(str( content[posistion].split()[1] ))) - 1 ): 

        
        print(posistion)
        print(content[posistion])
        tempList.append( ((content[posistion]).split())[1] ) # shit break line
        posistion += 1
        rows += 1
        
    matrix[1].append(tempList) 
    tempList =[]

    for count in range(int(str(content[posistion-columns])[1:2]) ):
        matrixPos = 0
        if str( ((content[posistion]).split())[0] ) == matrix[0][matrixPos]:
            if ( matrix[1][matrixPos] + int( ((content[posistion]).split())[1] ) ) >= 0:
                matrix[1][matrixPos] = matrix[1][matrixPos] + int(  str(content[posistion].split()[1])  + str(content[posistion].split()[2]) )
                print("YES")
            else:
                print("NO")
