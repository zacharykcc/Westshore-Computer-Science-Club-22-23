with open("chal.txt", 'r') as file:
    line_list = []
    for line in file:
        line_list.append(line.strip())

for count in range(len(line_list)):
    line_list[count] = line_list[count].lower()

for count in range(len(line_list)):
    hacker = line_list[count].find("hacker")
    print(hacker, end = "")
    print(": ", chr(hacker))
