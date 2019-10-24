'''
import cv2
import numpy as np

image= cv2.imread('image_0018.jpg')
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray= np.float32(gray)
harris_corners= cv2.cornerHarris(gray, 3, 3, 0.05)
kernel= np.ones((7,7),np.uint8)
harris_corners= cv2.dilate(harris_corners, kernel, iterations=2)
image[harris_corners > 0.025 * harris_corners.max()]= [255,127,127]
cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import cv2
import numpy as np

img= cv2.imread('image_0018.jpg')
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners= cv2.goodFeaturesToTrack(gray, 100, 0.01, 15)
print('corners:',len(corners))
for corner in corners:
	x,y= corner[0]
	x= int(x)
	y= int(y)
	cv2.rectangle(img, (x-10,y-10),(x+10,y+10),(0,255,0),2)
cv2.imshow("Cornes Found", img)
cv2.waitKey()
cv2.destroyAllWindows()