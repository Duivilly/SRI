import numpy as np
import cv2

#load image
name_image= 'image_0018'
img= cv2.imread(name_image+'.jpg', 0)

#set the size in the view of image into 40%
img= cv2.resize(img, (400, 400))

#load my histogram
histogramBorder= []
for i in range(256):
	histogramBorder.append(0)

histogramInside= []
for i in range(256):
	histogramInside.append(0)

#run the matriz
contBorder= 0
contInside= 0
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		if(j+2 < img.shape[1] and i+2 < img.shape[0]):
			ponto= int(img[i+1][j+1])
			v1= int(img[i][j])
			v2= int(img[i][j+2])
			v3= int(img[i+2][j])
			v4= int(img[i+2][j+2])
			if(ponto == v1 and ponto == v2 and ponto == v3 and ponto == v4):
				histogramInside[ponto]= histogramInside[ponto] + 1
				contInside= contInside + 1
			else:
				histogramBorder[ponto]= histogramBorder[ponto] + 1
				contBorder= contBorder + 1

#show image
#cv2.imshow("glass", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#save in file
f= open(name_image+'.txt','w')
out= histogramBorder+histogramInside
f.write(str(out))
f.close()

#infor image
#print ('Pixels Total: '+str(img.shape[0]*img.shape[1]))
#print ('Pixels in the Border: '+str(contBorder))
#print ('Pixels in the Inside: '+str(contInside))
#print ('Pixels Height: '+str(img.shape[0]))
#print ('Pixels Width : '+str(img.shape[1]))

#save image
#cv2.imwrite(name_image+'.png', img)
#print ('Image save')