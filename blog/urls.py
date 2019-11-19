from django.urls import path
from .views import ArticleView

urlpatterns =[
    path('home/', ArticleView.as_view(), name='home')
]