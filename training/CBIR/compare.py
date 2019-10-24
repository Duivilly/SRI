import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1= cv.imread('image_0019.jpg',0) # queryImage
img2= cv.imread('image_0018.jpg',0) # trainImage - 368points

# Initiate FAST detector
orb= cv.FastFeatureDetector_create()

# find the keypoints and descriptors with ORB
kp1= orb.detect(img1,None)
print('keypoints:',len(kp1))

matches= []

# Draw matches.
img3= cv.drawMatches(img1, kp1, img1, kp1, matches, None, None)
plt.imshow(img3),plt.show()

#cedd