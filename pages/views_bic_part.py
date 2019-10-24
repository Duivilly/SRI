import simplejson as json
import cv2
import os

from .models import BaseImage
from .forms import FormBaseImage
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from haystack.query import SearchQuerySet

def extractImageBIC_part(path):
	#load image
	#0       = gray
	#without = rgb
	path_dir= '/var/www/html/sri/'
	img= cv2.imread(path_dir+path, 0)

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
	limiar= 12
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
						# pixels da borda
						if(abs(pixel-v1) > limiar and abs(pixel-v2) > limiar and abs(pixel-v3) > limiar and abs(pixel-v4) > limiar):
							histogramBorder1[pixel]= histogramBorder1[pixel] + 1
							#img[i][j]= 0
						else:
							histogramInside1[pixel]= histogramInside1[pixel] + 1
							#img[i][j]= 255
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
						# pixels da borda
						if(abs(pixel-v1) > limiar and abs(pixel-v2) > limiar and abs(pixel-v3) > limiar and abs(pixel-v4) > limiar):
							histogramBorder2[pixel]= histogramBorder2[pixel] + 1
							#img[i][j]= 0
						else:
							histogramInside2[pixel]= histogramInside2[pixel] + 1
							#img[i][j]= 255
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
						# pixels da borda
						if(abs(pixel-v1) > limiar and abs(pixel-v2) > limiar and abs(pixel-v3) > limiar and abs(pixel-v4) > limiar):
							histogramBorder3[pixel]= histogramBorder3[pixel] + 1
							#img[i][j]= 0
						else:
							histogramInside3[pixel]= histogramInside3[pixel] + 1
							#img[i][j]= 255
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
						# pixels da borda
						if(abs(pixel-v1) > limiar and abs(pixel-v2) > limiar and abs(pixel-v3) > limiar and abs(pixel-v4) > limiar):
							histogramBorder4[pixel]= histogramBorder4[pixel] + 1
							#img[i][j]= 0
						else:
							histogramInside4[pixel]= histogramInside4[pixel] + 1
							#img[i][j]= 255
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
						# pixels da borda
						if(abs(pixel-v1) > limiar and abs(pixel-v2) > limiar and abs(pixel-v3) > limiar and abs(pixel-v4) > limiar):
							histogramBorder5[pixel]= histogramBorder5[pixel] + 1
							#img[i][j]= 0
						else:
							histogramInside5[pixel]= histogramInside5[pixel] + 1
							#img[i][j]= 255
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
	
	#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
	#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	#plt.show()
	return descriptor

'''	
def compareHistogramBIC_part(histogram1, histogram2, limiar):
    #bigger or equal 60% of similarity
    similarityMin= 0.6
    len_histogram1= len(histogram1[0])
    len_histogram2= len(histogram2[0])
    similarity= 0
    for n in range(len(histogram1)):
        equal= 0
        for i in range(len_histogram1):
            if abs(int(histogram1[n][i])-int(histogram2[n][i])) <= limiar:
            	equal= equal + 1
        similarity= (equal/len_histogram2)+similarity
    #5=parts
    similarityGet= similarity/5
    if similarityGet >= similarityMin:
        return [True, similarityGet]
    else:
        return [False, similarityGet]
'''

def compareHistogramBIC_part(histogram1, histogram2, limiar):
    md= 0
    for i in range(len(histogram1)):
    	for j in range(len(histogram2[0])):
        	md= abs(int(histogram1[i][j])-int(histogram2[i][j])) +md
    return [limiar, md]

def normalizeListBic_Part(part):
	bic_part= []
	for i in range(5):
		if i == 0:
			normalize= part.split(']')[i].replace("[[",'').replace(' ','').split(',')
		else:
			normalize= part.split(']')[i].replace(', [','').replace(' ','').split(',')
		bic_part.append(normalize)
	return bic_part

def orderBySimilarity(resultQueryImage):
	resultQueryImage.sort(key=lambda i:i[1])
	resultQueryImageOrder= list()
	for i in range(len(resultQueryImage)):
		resultQueryImageOrder.append(resultQueryImage[i][0])
#	resultQueryImageOrder.reverse()
	return resultQueryImageOrder[:30]

'''
def combinarTextImage(resultQueryText, resultQueryImage):
	resultQueryTextImage= list()
	for rqi in resultQueryImage:
		for rqt in resultQueryText:
			if rqi.id == rqt.object.id:
				resultQueryTextImage.append(rqt)
	return resultQueryTextImage[:30]
'''

def combinarTextImage(resultQueryText, resultQueryImage):
        resultQueryTextImage= list()
        resultQueryImagePart= list()
        resultQueryTextsPart= list()
        for rqi in resultQueryImage:
                count= 0
                for rqt in resultQueryText:
                        if rqi.id == rqt.object.id:
                                resultQueryTextImage.append(rqt.object)
                                count= count +1
                                break
                if count == 0:
                        resultQueryImagePart.append(rqi)
        for rqt in resultQueryText:
                count= 0
                for rti in resultQueryTextImage:
                        if rqt.object.id == rti.id:
                                count= count +1
                if count == 0:
                        resultQueryTextsPart.append(rqt.object)
        return resultQueryTextImage+resultQueryImagePart+resultQueryTextsPart

def home(request):
	context= {}
	resultQueryText= {}
	resultQueryImage= list()
	resultQueryTextImage= list()
	if request.method == 'POST':
		form= FormBaseImage(request.POST, request.FILES)
		if form.is_valid():
			context['noneResult']= False
			search_text= form.cleaned_data['search_text']
			search_image= form.cleaned_data['search_image']#search_image_name
			if search_text == '' and search_image == None:
				context['noneResult']= True
			else:
				#search_text contem texto para processar
				if search_text != '':
					context['is_text']= True
					#faz busca textual TBRI
					resultQueryText= SearchQuerySet().autocomplete(content_auto=search_text)
					total_query_texts= len(resultQueryText)
					if total_query_texts == 0:
						resultQueryText= {}
						context['is_text']= False
						context['noneResult']= True
					context['total_query_texts']= total_query_texts
				#search_image contem imagem para processar
				if search_image != None:
					context['is_image']= True
					#obtem a requisicao post da imagem
					search_image_upload= request.FILES['search_image']
					#guarda o caminha da imagem de upload
					pathImage= str('tmp/'+search_image_upload.name)
					#salva a imagem temporariamente no path
					path= default_storage.save(pathImage, ContentFile(search_image_upload.read()))
					#obtemm a imagem e adiciona no caminho path
					tmp_file= os.path.join(settings.MEDIA_ROOT, path)
					#obtem o vetor de caracteristica da imagem de upload
					extractImageUpload= extractImageBIC_part(pathImage)
					#load (BaseImage)
					allBaseImages= BaseImage.objects.all()
					#busca imagens semelhantes da upload com o BaseImage
					total_query_images= 30
					for q_img in allBaseImages:
						#processa a comparacao da imagem de upload com as da BaseImage
						resultcompareHistogramBIC= compareHistogramBIC_part(extractImageUpload, normalizeListBic_Part(q_img.descriptorBIC_part), True)
						if resultcompareHistogramBIC[0:1][0]:
							resultQueryImage.append((q_img, resultcompareHistogramBIC[1:2][0]))
							##print([q_img, resultcompareHistogramBIC[1:2][0]][1])
							#total_query_images= total_query_images +1
					#order by similarity
					resultQueryImage= orderBySimilarity(resultQueryImage)
					if total_query_images == 0:
						context['is_image']= False
						context['noneResult']= True
					context['total_query_images']= total_query_images
					#deleta a imagem de upload depois do processamento
					default_storage.delete(path)
				#combinacao da consulta textual com conteudo
				if search_text != '' and search_image != None:
					print('combinando...')
					context['is_text']= False
					context['is_image']= False
					context['is_text_image']= True
					resultQueryTextImage= combinarTextImage(resultQueryText, resultQueryImage)
					context['total_query_text_image']= len(resultQueryTextImage)
					if len(resultQueryTextImage) == 0:
						context['is_text_image']= False
						context['noneResult']= True
			#recria os campos do formulario de consulta
			form= FormBaseImage()
	else:
		form= FormBaseImage()
	context['form']= form
	context['resultQueryText']= resultQueryText
	context['resultQueryImage']= resultQueryImage
	context['resultQueryTextImage']= resultQueryTextImage
	return render(request, 'home.html', context)

import unicodedata
import re
def removeCharEspecials(palavra):
	#Unicode normalize transforma um caracter em seu equivalente em latin.
	nfkd= unicodedata.normalize('NFKD', palavra)
	palavraSemAcento= u"".join([c for c in nfkd if not unicodedata.combining(c)])
	#Usa expressão regular para retornar a palavra apenas com números, letras e espaço
	return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

def dropRepet(l):
	#l= ['copo','copos','copaiba','girafa','amor','copo','Copos','feliz']
	s= []
	if len(l) > 0:
		if len(s) == 0:
			s.append(l[0])
	#print(l)
	for i in range(1,len(l)):
		cont= False
		for j in range(len(s)):
			if l[i].lower() == s[j].lower():
				cont= True
		if not cont:
			s.append(l[i])
	#print(s)
	return s

#feature: melhorar o autocomplete para boas sugestoes
def autocomplete(request):
	suggestions= []
	if request.is_ajax:
		word= request.GET.get('terms','')
		print('word_to_search: '+word)
		if word != '':
			resultSuggestions= SearchQuerySet().autocomplete(content_auto=word)
			for rs in resultSuggestions:
				text_s= rs.object.search_text.split(" ")
				for w in range(len(text_s)):
					term= text_s[w]
					index_s= term.lower().find(word.lower())
					if index_s != -1:
						suggestions.append(removeCharEspecials(term))
	#drop of list repets
	suggestions= dropRepet(suggestions)
	#limit lenth suggestions
	suggestions= suggestions[:10]
	return HttpResponse(json.dumps(suggestions))
