import numpy as np
import cv2

#load image
name_image= 'image_0017'
img= cv2.imread(name_image+'.jpg', 0)

#set the size in the view of image into 40%
img= cv2.resize(img, (400, 400))

#load my histogramGlobal
histogramGlobal= []
for i in range(256):
	histogramGlobal.append(0)

#run the matriz
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		histogramGlobal[img[i][j]]= histogramGlobal[img[i][j]] + 1

#save in file
f= open(name_image+'_GHC.txt','w')
f.write(str(histogramGlobal))
f.close()