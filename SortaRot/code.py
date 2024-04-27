with open('chal.txt', 'r') as file:
    content = file.read()

def shift_letters(text, shift):
    shifted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            # Shift the character by the specified amount
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            shifted_text += shifted_char
        else:
            # If the character is not a letter, keep it unchanged
            shifted_text += char
    return shifted_text

flag = "zvoqfnw{uhk_ubk_ubwnwr_nznb}"

for count in range(1,26):
    print(shift_letters(flag, count))