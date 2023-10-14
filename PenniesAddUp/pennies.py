test_list = open("input.txt").readlines()

# printing original list


# Removing newline character from string
# using loop
res = []
for sub in test_list:
    res.append(sub.replace("\n", ""))

runs = int(res[0])
total = 0
def offset(lst, offset):
  return lst[offset:] + lst[:offset]

listPosistion = 1
finalPosistion = 0

for count in range(runs):
    valueAndWords = res[listPosistion]
    valueAndWords = list(valueAndWords.split(" "))
    valueAndWords = [int(valueAndWords[0]), int(valueAndWords[1])]
    finalPosistion = listPosistion + valueAndWords[1]
    alphabet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    offsetted = offset(alphabet,valueAndWords[0])
    a = int(offsetted[0])
    b = int(offsetted[1])
    c = int(offsetted[2])
    d = int(offsetted[3])
    e = int(offsetted[4])
    f = int(offsetted[5])
    g = int(offsetted[6])
    h = int(offsetted[7])
    i = int(offsetted[8])
    j = int(offsetted[9])
    k = int(offsetted[10])
    l = int(offsetted[11])
    m = int(offsetted[12])
    n = int(offsetted[13])
    o = int(offsetted[14])
    p = int(offsetted[15])
    q = int(offsetted[16])
    r = int(offsetted[17])
    s = int(offsetted[18])
    t = int(offsetted[19])
    u = int(offsetted[20])
    v = int(offsetted[21])
    w = int(offsetted[22])
    x = int(offsetted[23])
    y = int(offsetted[24])
    z = int(offsetted[25])

    for count in range(valueAndWords[1]):
        word = res[listPosistion+1]
        listPosistion += 1
        word = list(word)
        for count in range(len(word)):
            total = 0
            if word[0] == "A":
                total += a
            if word[0] == "B":
                total += b
            if word[0] == "C":
                total += c
            if word[0] == "D":
                total += d
            if word[0] == "E":
                total += e
            if word[0] == "F":
                total += f
            if word[0] == "G":
                total += g
            if word[0] == "H":
                total += h
            if word[0] == "I":
                total += i
            if word[0] == "J":
                total += j
            if word[0] == "K":
                total += k
            if word[0] == "L":
                total += l
            if word[0] == "M":
                total += m
            if word[0] == "N":
                total += n
            if word[0] == "O":
                total += o
            if word[0] == "P":
                total += p
            if word[0] == "Q":
                total += q
            if word[0] == "R":
                total += r
            if word[0] == "S":
                total += s
            if word[0] == "T":
                total += t
            if word[0] == "U":
                total += u
            if word[0] == "V":
                total += v
            if word[0] == "W":
                total += w
            if word[0] == "X":
                total += x
            if word[0] == "Y":
                total += y
            if word[0] == "Z":
                total += z
        print(total)
        listPosistion = finalPosistion







