from rest_framework.serializers import ModelSerializer
from .models import Article


class ArticleSerializer(ModelSerializer):
    """
    Serializer class for Article model
    """
    class Meta:
        """
        Metadata about Article model
        """
        model = Article
        fields = '__all__'
