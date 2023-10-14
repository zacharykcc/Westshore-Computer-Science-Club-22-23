

rot3 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'DEFGHIJKLMNOPdefghijklmnopQRSTUVWXYZABCqrstuvwxyzabc')
#print('Hello World!'.translate(rot13))

rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

Flag = "zvoqfnw{uhk_ubk_ubwnwr_nznb}"

print("z".translate(rot3))