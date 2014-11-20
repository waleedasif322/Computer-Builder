"""
This module is for the use of haystack
"""
from haystack import indexes
from builds.models import BuildsTable

class BuildIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Buildindex class for Haystack
    """
    text = indexes.CharField(document=True, use_template=True)
    content_auto = indexes.EdgeNgramField(model_attr='name')    
    def get_model(self):
        """
        This is how haystack returns objects after search
        """
        return BuildsTable

    def index_queryset(self, using=None):
        """
        users can only search public pictures
        """
        builds = BuildsTable.objects.all().filter(access_r='pub')
        return builds
