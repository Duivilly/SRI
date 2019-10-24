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

def extractImageBIC(pathImage):
	#load image
	path_dir= '/var/www/html/sri/'
	img= cv2.imread(path_dir+pathImage, 0)

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
	limiar= 12
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
				#pixels da borda
				if(abs(ponto-v1) > limiar and abs(ponto-v2) > limiar and abs(ponto-v3) > limiar and abs(ponto-v4) > limiar):
					histogramBorder[ponto]= histogramBorder[ponto] + 1
					contInside= contInside + 1
					img[i+1][j+1]= 0   #black
				else:
					histogramInside[ponto]= histogramInside[ponto] + 1
					contBorder= contBorder + 1
					img[i+1][j+1]= 255 # white
	out= histogramBorder+histogramInside
	return out

def compareHistogramBIC(histogram1, histogram2, limiar):
    #bigger or equal 30% from similarity of color
    equal= 0
    similarityMin= 0.5
    len_histogram1= len(histogram1)
    len_histogram2= len(histogram2)
    for i in range(len_histogram1):
        if abs(int(histogram1[i])-int(histogram2[i])) <= limiar:
        	equal= equal + 1
    similarity= equal/len_histogram2
    if similarity >= similarityMin:
        return [True, similarity]
    else:
        return [False, similarity]

def normalizeListBic(strList):
	strList= strList.split(',')
	l= list()
	for i in range(len(strList)):
		n= strList[i].replace("'","")
		n= n.replace(" ","")
		n= n.replace("[","")
		n= n.replace("]","")
		l.append(n)
	return l

def orderBySimilarity(resultQueryImage):
	resultQueryImage.sort(key=lambda i:i[1])
	resultQueryImageOrder= list()
	for i in range(len(resultQueryImage)):
		resultQueryImageOrder.append(resultQueryImage[i][0])
	resultQueryImageOrder.reverse()
	return resultQueryImageOrder[:30]

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
					extractImageUpload= extractImageBIC(pathImage)
					#load (BaseImage)
					allBaseImages= BaseImage.objects.all()
					#busca imagens semelhantes da upload com o BaseImage
					total_query_images= 0
					for q_img in allBaseImages:
						#processa a comparacao da imagem de upload com as da BaseImage
						resultcompareHistogramBIC= compareHistogramBIC(extractImageUpload, normalizeListBic(q_img.descriptorBIC), 16)
						if resultcompareHistogramBIC[0:1][0]:
							resultQueryImage.append((q_img, resultcompareHistogramBIC[1:2][0]))
							##print([q_img, resultcompareHistogramBIC[1:2][0]][1])
							total_query_images= total_query_images +1
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
