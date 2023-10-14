hexxed = input()
hexxed = hexxed.split()

for count in range(len(hexxed)):
    current_string = hexxed[count]
    current_string = current_string[2:]
    hexxed[count] = current_string

for count in range(0, 255):
    
    key = count
    output = ""

    for count in range(len(hexxed)):
        decimal_number = (int(str(hexxed[count]), 16) ^ key)
        unicode_character = chr(decimal_number)
        
        key += 1
        key %= 0x100
        
        output += unicode_character
    print(output)