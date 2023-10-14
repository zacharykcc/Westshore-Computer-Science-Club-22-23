hexxed = input()
hexxed = hexxed.split()

for count in range(len(hexxed)):
    current_string = hexxed[count]
    current_string = current_string[2:]
    hexxed[count] = current_string



'''onlyhex = hexxed[0]
for count in range(len(hexxed) - 1):
    count += 1
    onlyhex += " " + hexxed[count]
'''



for count in range(len(hexxed)):
    decimal_number = (int(str(hexxed[count]), 16) ^ int("83", 16))
    unicode_character = chr(decimal_number)
    print(unicode_character, end = "")