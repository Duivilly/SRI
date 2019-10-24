import os

#1.update path dir
#2.indexing images

def update_path_dir(path):
	config= open('build.gradle','r')
	path_flag= True
	new_config= ''
	line= True
	while line:
		line= config.readline()
		if line.find('args') != -1 and path_flag:
			new_config= new_config + "    args '"+path+"'" + '\n'
			path_flag= False
		else:
			new_config= new_config + line
		if line == '':
			line= False
	config.close()
	config= open('build.gradle','w')
	config.write(new_config)
	config.close()
	print('path dir update.')

# show path dir to IndexingImages
path= '/home/duivilly/Dropbox/sri/base'
update_path_dir(path)

# execute to IndexingImages
os.system('./gradlew task runIndexing')