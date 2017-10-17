import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55,55]
img[55,55] = [0,0,0]
print(px)

roi = img[100:150, 100:150]
img[100:150, 100:150] = [0,0,0]
print(roi)

watch_moha = img[37:111, 107:194]
img[0:74, 0:87] = watch_moha


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
