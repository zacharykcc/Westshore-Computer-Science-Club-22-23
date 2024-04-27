import matplotlib.pyplot as plt

file_path = 'chal.txt'
with open(file_path, 'r') as file:
    content = file.read().splitlines()


for count in range(len(content)):
    XandY = content[count].split(",")
    XandY[0] = int(XandY[0])
    XandY[1] = int(XandY[1])
    print(XandY[0],XandY[1])