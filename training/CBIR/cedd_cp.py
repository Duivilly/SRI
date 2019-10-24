import cv2
import numpy as np
import matplotlib.pyplot as plt

#load image
#0       = gray
#without = rgb
img= cv2.imread('image_0018.jpg', 0)

#edge histogram (texture)
img= cv2.Canny(img,100,200)

#set the size in the view of image into 40%
img= cv2.resize(img, (400, 400))

#load histogram opencv
plt.hist(img.ravel(),256,[0,256])

#descriptor BIC
def extractImageBIC(pathImage):
	#load image
	img= cv2.imread(pathImage, 0)

	#set the size of image into 40% in the view
	img= cv2.resize(img, (400, 400))

	#load my histogram of border
	histogramBorder= []
	for i in range(256):
		histogramBorder.append(0)

	#load my histogram of inside
	histogramInside= []
	for i in range(256):
		histogramInside.append(0)

	#run the matriz
	contBorder= 0
	contInside= 0
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			#inside
			if(j+2 < img.shape[1] and i+2 < img.shape[0]):
				ponto= int(img[i+1][j+1])
				#os quatro vizinhos mais proximos
				v1= int(img[i][j])
				v2= int(img[i][j+2])
				v3= int(img[i+2][j])
				v4= int(img[i+2][j+2])
				#os pixels sao da mesma cor entao estao no interior senao estao na borda
				if(ponto == v1 and ponto == v2 and ponto == v3 and ponto == v4):
					histogramInside[ponto]= histogramInside[ponto] + 1
					contInside= contInside + 1
				else:
					histogramBorder[ponto]= histogramBorder[ponto] + 1
					contBorder= contBorder + 1
	out= histogramBorder+histogramInside
	return out

#load my histogram
histogram1= []
for i in range(256):
	histogram1.append(0)

histogram2= []
for i in range(256):
	histogram2.append(0)

histogram3= []
for i in range(256):
	histogram3.append(0)

histogram4= []
for i in range(256):
	histogram4.append(0)

histogram5= []
for i in range(256):
	histogram5.append(0)

histogram6= []
for i in range(256):
	histogram6.append(0)

w= img.shape[1]
h= img.shape[0]
for i in range(h):
	for j in range(w):
		#escurece particionamento 1
		if(j >= 0 and j <= w/2):#col
			if(i >= 0 and i <= h/2):#lin
				#img[i][j]= 255
				histogram1[int(img[i][j])]= histogram1[int(img[i][j])] + 1
		#escurece particionamento 2
		if(j >= w/2 and j <= w):#col
			if(i >= 0 and i <= h/2):#lin
				#img[i][j]= 0
				histogram2[int(img[i][j])]= histogram2[int(img[i][j])] + 1
		#escurece particionamento 3
		if(j >= 0 and j <= w/2):#col
			if(i >= h/2 and i <= h):#lin
				#img[i][j]= 0
				histogram3[int(img[i][j])]= histogram3[int(img[i][j])] + 1
		#escurece particionamento 4
		if(j >= w/2 and j <= w):#col
			if(i >= h/2 and i <= h):#lin
				#img[i][j]= 255
				histogram4[int(img[i][j])]= histogram4[int(img[i][j])] + 1
		#escurece particionamento 5
		if(j >= w/4 and j <= (w/4)*3):#col
			if(i >= h/4 and i <= (h/4)*3):#lin
				#img[i][j]= 255
				histogram5[int(img[i][j])]= histogram5[int(img[i][j])] + 1
		#escurece particionamento 6 (global)
		if(True):#col
			if(True):#lin
				#img[i][j]= 255
				histogram6[int(img[i][j])]= histogram6[int(img[i][j])] + 1

#show from opencv
#plt.show()

#infor image
print ('Pixels Height: '+str(img.shape[0]))
print ('Pixels Width : '+str(img.shape[1]))

plt.subplot(121)
plt.imshow(img, cmap= 'gray')
plt.title('Image')
plt.xticks([])
plt.yticks([])
plt.show()