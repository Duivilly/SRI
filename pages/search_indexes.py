import datetime
from haystack import indexes
from .models import BaseImage

class BaseImageIndex(indexes.SearchIndex, indexes.Indexable):
    text= indexes.CharField(document=True, use_template=True)
    search_text= indexes.CharField(model_attr='search_text')
    content_auto= indexes.EdgeNgramField(model_attr='search_text')

    def get_model(self):
        return BaseImage

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

#na indexacao nao esta sendo levado em consideracao os acentos segundo minha percepcao