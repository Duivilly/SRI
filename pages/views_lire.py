import simplejson as json
#import subprocess
#path_dir= subprocess.getstatusoutput('pwd')[1]
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

#1.update pathImage dir
#2.search images

def update_pathImage_dir(pathImage, path_dir):
	config= open(path_dir+'build.gradle','r')
	pathImage_flag= 0
	new_config= ''
	line= True
	while line:
		line= config.readline()
		if line.find('args') != -1 and pathImage_flag != 2:
			pathImage_flag= pathImage_flag +1
			if pathImage_flag == 2:
				new_config= new_config + "    args '"+pathImage+"'" + '\n'
			else:
				new_config= new_config + line
		else:
			new_config= new_config + line
		if line == '':
			line= False
	config.close()
	config= open(path_dir+'/build.gradle','w')
	config.write(new_config)
	config.close()
	print('pathImage dir update.')

def runSearch(pathImage, path_dir):
	update_pathImage_dir(pathImage, path_dir)
	print('searching...')
	# execute to IndexingImages
	os.system(path_dir+'./gradlew task runSearch > resultRunSearch.txt')
	print('search complete.')
	print('export resultRunSearch.txt')

# get result run search
def get_pathImages_dir(pathImage, path_dir):
	runSearch(pathImage, path_dir)
	config= open(path_dir+'resultRunSearch.txt','r')
	resultRunSearch= []
	line= True
	while line:
		line= config.readline()
		if line.find('.jpg') != -1:
			img_part= line.split('/')
			id_url= img_part[len(img_part)-1].replace('\n','')
			resultRunSearch.append(id_url)
		if line == '':
			line= False
	config.close()
	print('complete path dir images.')
	return resultRunSearch

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
					#obtem a imagem e adiciona no caminho path
					tmp_file= os.path.join(settings.MEDIA_ROOT, path)
					#path dir
					path_dir= '/var/www/html/sri/'
					#list of images CEDD
					imagesOrderCEDD= get_pathImages_dir(path_dir+pathImage, path_dir)[:30]#recupera as 30 primeiras
					#busca imagens semelhantes da upload com o BaseImage
					total_query_images= 0
					for count_cedd in range(len(imagesOrderCEDD)):
						resultQueryImagesCEDD= BaseImage.objects.search('images/'+imagesOrderCEDD[count_cedd])
						for getImagesCEDD in resultQueryImagesCEDD:
							resultQueryImage.append(getImagesCEDD)
						total_query_images= total_query_images +1
					#order by similarity
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
#
#melhorar os paths (pathImage)
