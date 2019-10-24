import matplotlib.pyplot as plt
import sqlite3
import cv2
import os

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

def extractImageBIC_part(path):
	#load image
	#0       = gray
	#without = rgb
	img= cv2.imread(path, 0)

	#edge histogram (texture)
	#img= cv2.Canny(img,100,200)

	#set the size in the view of image into 40%
	img= cv2.resize(img, (400, 400))

	#load histogram opencv
	#plt.hist(img.ravel(),256,[0,256])

	#load my histograms bic (border/interior)
	histogramBorder1= []
	for i in range(256):
		histogramBorder1.append(0)

	histogramInside1= []
	for i in range(256):
		histogramInside1.append(0)

	#load my histograms bic 2
	histogramBorder2= []
	for i in range(256):
		histogramBorder2.append(0)

	histogramInside2= []
	for i in range(256):
		histogramInside2.append(0)

	#load my histograms bic 3
	histogramBorder3= []
	for i in range(256):
		histogramBorder3.append(0)

	histogramInside3= []
	for i in range(256):
		histogramInside3.append(0)

	#load my histograms bic 4
	histogramBorder4= []
	for i in range(256):
		histogramBorder4.append(0)

	histogramInside4= []
	for i in range(256):
		histogramInside4.append(0)

	#load my histograms bic 5
	histogramBorder5= []
	for i in range(256):
		histogramBorder5.append(0)

	histogramInside5= []
	for i in range(256):
		histogramInside5.append(0)

	w= img.shape[1]
	h= img.shape[0]
	for i in range(h):
		for j in range(w):
			#escurece particionamento 1
			if(j >= 0 and j <= w/2):#col
				if(i >= 0 and i <= h/2):#lin
					#img[i][j]= 255 #branco
					#bic part1
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside1[pixel]= histogramInside1[pixel] + 1
						else:
							histogramBorder1[pixel]= histogramBorder1[pixel] + 1
			#escurece particionamento 2
			if(j >= w/2 and j <= w):#col
				if(i >= 0 and i <= h/2):#lin
					#img[i][j]= 0
					#bic part2
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside2[pixel]= histogramInside2[pixel] + 1
						else:
							histogramBorder2[pixel]= histogramBorder2[pixel] + 1
			#escurece particionamento 3
			if(j >= 0 and j <= w/2):#col
				if(i >= h/2 and i <= h):#lin
					#img[i][j]= 0
					#bic part3
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside3[pixel]= histogramInside3[pixel] + 1
						else:
							histogramBorder3[pixel]= histogramBorder3[pixel] + 1
			#escurece particionamento 4
			if(j >= w/2 and j <= w):#col
				if(i >= h/2 and i <= h):#lin
					#img[i][j]= 255
					#bic part4
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside4[pixel]= histogramInside4[pixel] + 1
						else:
							histogramBorder4[pixel]= histogramBorder4[pixel] + 1
			#escurece particionamento 5
			if(j >= w/4 and j <= (w/4)*3):#col
				if(i >= h/4 and i <= (h/4)*3):#lin
					#img[i][j]= 255
					#bic part5
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside5[pixel]= histogramInside5[pixel] + 1
						else:
							histogramBorder5[pixel]= histogramBorder5[pixel] + 1
	descriptor= []
	#add descriptor 1
	descriptor.append(histogramBorder1+histogramInside1)
	#add descriptor 2
	descriptor.append(histogramBorder2+histogramInside2)
	#add descriptor 3
	descriptor.append(histogramBorder3+histogramInside3)	
	#add descriptor 4
	descriptor.append(histogramBorder4+histogramInside4)
	#add descriptor 5
	descriptor.append(histogramBorder5+histogramInside5)
	return descriptor

def extractHistogramORB(path):
	# trainImage - 368points
	img= cv2.imread(path, 0)
	# Initiate ORB detector
	orb= cv2.ORB_create()
	# find the keypoints and descriptors with ORB
	kp1, des1= orb.detectAndCompute(img, None)
	descriptorORB= []
	keys= des1
	if str(keys) != 'None':
		for i in range(len(des1)):
			q= des1[i]
			q= str(q).replace('[','').replace(']','')
			q= q.split(' ')
			r= []
			for j in range(len(q)):
				if q[j] != '':
					r.append(q[j].replace('\n',''))
			descriptorORB.append(r)
	return descriptorORB

# connect db
connection= sqlite3.connect('db.sqlite3')
db= connection.cursor()

down= open('downloads_fail.txt','w')
base= open('base.txt','r')
# 8942
count= 0
# elimine title
line_data= base.readline().replace('%,','%').split('%')
for i in range(3):
	line_data= base.readline().replace('%,','%').split('%')
	# 1=url and 2=text
	url= str(line_data[1])
	part_url= str(line_data[1]).split('/')
	id_url= part_url[len(part_url)-1]
	text= str(line_data[2]).replace('\n','')[1:]
	# verifique se ja foi baixado
	if os.system('ls | grep '+id_url) != 0:
		# obter imagem da web
		os.system('wget '+url)
		if os.system('ls | grep '+id_url) == 256:
			down.write('download:'+url+'\n')
	try:
		# insert into db
		db.execute("""INSERT INTO pages_baseimage(id, search_image, search_text, descriptorBIC, descriptorBIC_part) VALUES (?,?,?,?,?);""", (count, 'images/'+id_url, text, str(extractImageBIC(id_url)), str(extractImageBIC_part(id_url))))
		# update into db
		#db.execute(""" UPDATE pages_baseimage SET search_image = ? WHERE descriptorBIC_part = ? """,(('images/'+id_url), str(descriptorBIC_part(id_url))))
		# save
		connection.commit()
	except ValueError:
		down.write('insert:'+url+'\n')
	count= count +1
	print('***Processing:',count)
connection.close()
down.close()
base.close()
print('saved.')