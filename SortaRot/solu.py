def rot_back_3(char):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
    else:
        return char

def rot_back_13(char):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') - 13) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') - 13) % 26 + ord('A'))
    else:
        return char

def apply_rotations(input_string):
    result = ""
    char_count = 0  # Counter to keep track of non-whitespace characters
    for i in range(len(input_string)):
        if input_string[i].isspace():  # Check if the character is whitespace
            result += " "  # Preserve whitespace characters
        else:
            char_count += 1  # Increment the character count for non-whitespace characters
            if char_count % 2 == 0:  # Check if the current non-whitespace character is at an even position
                result += rot_back_13(input_string[i])  # Rotate even-indexed characters backward by 13 positions
            else:
                result += rot_back_3(input_string[i])   # Rotate odd-indexed characters backward by 3 positions
    return result

#input_string = input("Enter a string: ")
input_string = "L kbsr lrh nurq'w grfbgvqt gkvv el udag.  L prda, fbpr bq, jh deh la przshwru vplrqph fyxo.  Lrh fkbxyg fbpr hs zvwu n ffelcw wudg wxfw narpnf gkvv rhw rafr zr sltxeh rhw wudg gkrur nur bqyb 2 nvqqv rs ergdglbq jblaj ra uheh, bqr sre wuh hiha pknunfghev, nqq bqr sre gkr bgq pknunfghev.  Dabjdlv, uheh lf lrhu iydt: zvoqfnw{uhk_ubk_ubwnwr_nznb}"
output_string = apply_rotations(input_string)
print("Transformed string:", output_string)