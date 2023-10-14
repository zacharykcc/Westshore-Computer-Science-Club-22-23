import os

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

combined = []

for count in range(100):
    folder = ("./chal/"+str(count))
    sub_folders = os.listdir(folder)
    
    for count in range(len(sub_folders)):
        combined.append(sub_folders[count])


for count in range(len(combined)):
    if combined[count] == "a":
        a += 1
    if combined[count] == "b":
        b += 1
    if combined[count] == "c":
        c += 1
    if combined[count] == "d":
        d += 1
    if combined[count] == "e":
        e += 1
    if combined[count] == "f":
        f += 1
    if combined[count] == "g":
        g += 1
    if combined[count] == "h":
        h += 1
    if combined[count] == "i":
        i += 1
    if combined[count] == "j":
        j += 1
    if combined[count] == "k":
        k += 1
    if combined[count] == "l":
        l += 1
    if combined[count] == "m":
        m += 1
    if combined[count] == "n":
        n += 1
    if combined[count] == "o":
        o += 1
    if combined[count] == "p":
        p += 1
    if combined[count] == "q":
        q += 1
    if combined[count] == "r":
        r += 1
    if combined[count] == "s":
        s += 1
    if combined[count] == "t":
        t += 1
    if combined[count] == "u":
        u += 1
    if combined[count] == "v":
        v += 1
    if combined[count] == "w":
        w += 1
    if combined[count] == "x":
        x += 1
    if combined[count] == "y":
        y += 1
    if combined[count] == "z":
        z += 1


solution = ["z","k","n","s","p","j","q","y","o","m","f","i","e","a","u","r","h","d","w","b","c","v","x","l"]
