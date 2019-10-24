import os

#1.update pathImage dir
#2.search images

def update_pathImage_dir(pathImage):
	config= open('build.gradle','r')
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
	config= open('build.gradle','w')
	config.write(new_config)
	config.close()
	print('pathImage dir update.')

def runSearch(pathImage):
	update_pathImage_dir(pathImage)
	print('searching...')
	# execute to IndexingImages
	os.system('./gradlew task runSearch > resultRunSearch.txt')
	print('search complete.')
	print('export resultRunSearch.txt')

# obter result run search
def get_pathImages_dir(pathImage):
	runSearch(pathImage)
	config= open('resultRunSearch.txt','r')
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

# show pathImage dir to IndexingImages
pathImage= '/home/duivilly/Dropbox/sri/base/image_0056.jpg'
print(get_pathImages_dir(pathImage))
# search in (resultQueryImagesCEDD= BaseImage.objects.search(images+'/'+id_url))