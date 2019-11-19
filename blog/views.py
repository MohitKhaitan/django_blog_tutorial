from django.views.decorators.cache import never_cache
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article


class ArticleView(APIView):
    """
    To display the list of articles
    """
    @never_cache
    def get(self, request: Request) -> Response:
        """
        Returns a list of articles present
        :param request: Http request
        :return: List of articles
        """
        data = Article.objects.all()
        serializer = ArticleSerializer(data)

        return Response(serializer.data, status=status.HTTP_200_OK)




    model = Article
    template_name = 'home.html'
