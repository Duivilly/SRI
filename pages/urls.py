from django.urls import path
from .import views_bic_part
from .import views_lire
from .import views_bic

avaliable= 'views_bic'
print('Running:',avaliable)

if avaliable == 'views_bic':

	urlpatterns = [
	    path('index/', views_bic.home, name='index'),
	    path('search/', views_bic.autocomplete, name='search'),
	]

if avaliable == 'views_bic_part':

	urlpatterns = [
	    path('index/', views_bic_part.home, name='index'),
	    path('search/', views_bic_part.autocomplete, name='search'),
	]

if avaliable == 'views_lire':

	urlpatterns = [
	    path('index/', views_lire.home, name='index'),
	    path('search/', views_lire.autocomplete, name='search'),
	]
