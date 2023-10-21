with open('input.txt', 'r') as file:
    words = file.read().split()

with open('AIRPORT_LIST.TXT', 'r'):
    abrev = file.read().split()


for count in range(len(words)):
    if words[count] == abrev[count]:
        words[count] = (abrev[count + 2]
            