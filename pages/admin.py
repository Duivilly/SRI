from django.contrib import admin

# Register your models here.
from .models import BaseImage

class SearchAdmin(admin.ModelAdmin):
    list_display= ['search_image', 'search_text']
    search_fields= ['search_text']
admin.site.register(BaseImage, SearchAdmin)