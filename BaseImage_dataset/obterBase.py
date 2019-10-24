# file= open('/home/duivilly/Área de Trabalho/dataset_images_texts/images_2016_08/validation/images.csv','r')
# validation set (167.057 images)
import csv

out= open('base.txt','w')
image_text = []
cont_plant = 0
cont_ground= 0
cont_card  = 0
cont_home  = 0
cont_artist= 0
cont_spide = 0
cont_face  = 0
count      = 0
# 10=url and 7=text
# training set (9.011.219 images)
with open('/home/duivilly/Área de Trabalho/dataset_images_texts/images_2016_08/train/images.csv', newline='') as csvfile:
    spamreader= csv.reader(csvfile, delimiter=',') # separe por virgula
    for line_data in spamreader:                   # o modulo csv detectara novas linhas automaticamente
        term= False
        url = str(line_data[10])
        text= str(line_data[7])
        if count%1000 == 0:
            # if exist url
            if url != '':
                # write data
                out.write('%'+url+'%'+', '+text+'\n')
            term= True
        if term == False:
            min_= 20
            contain= False
            if cont_plant < min_ and text.find('plant') != -1:
                contain= True
                cont_plant= cont_plant +1
            elif cont_ground < min_ and text.find('ground') != -1:
                contain= True
                cont_ground= cont_ground +1
            elif cont_card < min_ and text.find('card') != -1:
                contain= True
                cont_card= cont_card +1
            elif cont_home < min_ and text.find('home') != -1:
                contain= True
                cont_home= cont_home +1
            elif cont_artist < min_ and text.find('artist') != -1:
                contain= True
                cont_artist= cont_artist +1
            elif cont_spide < min_ and text.find('spide') != -1:
                contain= True
                cont_spide= cont_spide +1
            elif cont_face < min_ and text.find('face') != -1:
                contain= True
                cont_face= cont_face +1
            if contain:
                # if exist url
                if url != '':
                    # write data
                    out.write('%'+url+'%'+', '+text+'\n')
        # count total proccessad and print
        count= count +1
        print('count:',count)
        # 9011219
        if count == 9011219:
            break
out.close()