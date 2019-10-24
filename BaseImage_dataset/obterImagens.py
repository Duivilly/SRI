import os
down= open('downloads_fail.txt','w')
base= open('base.txt','r')
# 8943
count= 0
for i in range(8943):
	line_data= base.readline().replace('%,','%').split('%')
	# 1=url and 2=text
	url= str(line_data[1])
	part_url= str(line_data[1]).split('/')
	id_url= part_url[len(part_url)-1]
	text= str(line_data[2]).replace('\n','')[1:]
	if i != 0:
		# verifica se ja foi baixado
		if os.system('ls | grep '+id_url) != 0:
			# obter imagem da web
			os.system('wget '+url)
			if os.system('ls | grep '+id_url) == 256:
				down.write(url+'\n')
		count= count +1
		print('***Download:',count)	
down.close()
base.close()
print('saved.')