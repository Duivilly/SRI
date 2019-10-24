from django.db import models

# python3 manage.py makemigrations (cria a tabela)
# python3 manage.py migrate (aplica a tabela ao banco)
# pip install Pillow

class SearchManager(models.Manager):
	#from pages.models import BaseImage
	#BaseImage.objects.search('colher')
	def search(self, query):
		return self.get_queryset().filter(models.Q(search_image__icontains=query))

class BaseImage(models.Model):
	#campo de pesquisa por imagem (path da imagem)
	search_image= models.ImageField(upload_to='tmp', verbose_name='path_imagem', null=True, blank=True)
	#campo de pesquisa por texto
	search_text= models.TextField('search_text', null=True, blank=True)
	#campo para o vetor de caracteristicas da imagem BIC
	descriptorBIC= models.TextField('descriptorBIC', null=True, blank=True)
	#campo para o vetor de caracteristicas da imagem BIC part
	descriptorBIC_part= models.TextField('descriptorBIC_part', null=True, blank=True)
	#objeto para consulta personalizada
	objects= SearchManager()

	def __str__(self):
		return self.search_text

	#def get_absolute_url(self):
	#	return reverse("resultQueryText:detail", kwargs={"slug": self.slug})

	class Meta:
		verbose_name= 'SearchImagem'
		verbose_name_plural = 'BaseImage'
		ordering = ['search_image']