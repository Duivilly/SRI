import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1= cv.imread('image_0019.jpg',0) # queryImage
img2= cv.imread('image_copo.jpg',0) # trainImage - 368points

# Initiate ORB detector
orb= cv.ORB_create()

# find the keypoints and descriptors with ORB
kp1, des1= orb.detectAndCompute(img1,None)
print('keypoints1:',len(des1))
kp2, des2= orb.detectAndCompute(img2,None)
print('keypoints2:',len(des2))

# create BFMatcher object
bf= cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches= bf.match(des1,des2)

# Sort them in the order of their distance.
matches= sorted(matches, key= lambda x:x.distance)
print('keypoints:',len(matches))

# Draw matches.
img3= cv.drawMatches(img1, kp1, img2, kp2, matches, None, None)
plt.imshow(img3),plt.show()