import imp
from django.urls import path
from .views import  ArticleAPIView, ArticleDetails


urlpatterns = [
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    #path('details/<int:pk>', article_detail)
    path('details/<int:id>',ArticleDetails.as_view())

]
