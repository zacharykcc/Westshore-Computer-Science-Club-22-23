preFlag = "zvoqfnw{uhk_ubk_ubwnwr_nznb}"
preStory = "L kbsr lrh nurq'w grfbgvqt gkvv el udag.  L prda, fbpr bq, jh deh la przshwru vplrqph fyxo.  Lrh fkbxyg fbpr hs zvwu n ffelcw wudg wxfw narpnf gkvv rhw rafr zr sltxeh rhw wudg gkrur nur bqyb 2 nvqqv rs ergdglbq jblaj ra uheh, bqr sre wuh hiha pknunfghev, nqq bqr sre gkr bgq pknunfghev.  Dabjdlv, uheh lf lrhu iydt: zvoqfnw{uhk_ubk_ubwnwr_nznb}"
preStory = preStory.split()

rot3 = str.maketrans(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    'DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc'
    )

rot13 = str.maketrans(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
)


final = ""


for count in range(len(preStory)):
    if (count % 2) == 0:
        for i in range(len(preStory[count])):
            if (i % 2) == 0:
                final +=preStory[i].translate(rot3)
            if (i % 2) == 0:
                final +=preStory[i].translate(rot3)
    if (count % 2) == 1:
        for i in range(len(preStory[count])):
            if (i % 2) == 0:
                final +=preStory[i].translate(rot13)
            if (i % 2) == 0:
                final +=preStory[i].translate(rot13)




#        final += preStory[count].translate(rot3)


#        final += preStory[count].translate(rot13)

print(final)