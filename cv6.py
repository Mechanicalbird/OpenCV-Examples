import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('11.png')
img2 = cv2.imread('22.png')

#add = img1+img2
#add = cv2.add(img1,img2)

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('weighted',weighted)

#cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
