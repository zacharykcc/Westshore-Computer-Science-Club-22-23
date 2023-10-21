'''from stegano import lsb

secret = lsb.reveal("chal.png")
print(secret)

'''


from LSBSteg import *
import cv2

im = cv2.imread("chal.png")
steg = LSBSteg(im)
print("Decoded:",steg.decode_text())