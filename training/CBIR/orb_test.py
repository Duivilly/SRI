import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1= cv.imread('image_0020.jpg',0) # queryImage

# Initiate ORB detector
orb= cv.ORB_create()

# find the keypoints and descriptors with ORB
kp1, des1= orb.detectAndCompute(img1,None)

orb_descriptor= []
for i in range(2):
	q= des1[i]
	q= str(q).replace('[ ','').replace(']','')
	q= q.split(' ')
	r= []
	for j in range(len(q)):
		if q[j] != '':
			r.append(q[j].replace('\n',''))
	orb_descriptor.append(r)
print(orb_descriptor)