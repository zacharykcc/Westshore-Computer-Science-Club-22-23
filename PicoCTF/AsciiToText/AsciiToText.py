file_path = 'ascii.txt'

lines_list = []

with open(file_path, 'r') as file:
    for line in file:
        lines_list.append(line.strip())

for count in range(len(lines_list)):
    print(chr(int(lines_list[count])), end='')
    count += 1