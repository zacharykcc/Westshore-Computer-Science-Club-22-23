instructions = input("Instructions: ").split(",")


for count in range(len(instructions)):
    instructions[count] = int(instructions[count])

# ['1', '0', '0', '3', '99']


    if instructions[i] == 1:
        instructions[instructions[i+3]]  = instructions[instructions[i+1]] + instructions[instructions[i+2]]

    if instructions[i] == 2:
        instructions[instructions[i+3]] = instructions[instructions[i+1]] * instructions[instructions[i+2]]

    if instructions[i] == 99:
        break


    print(instructions[i])



