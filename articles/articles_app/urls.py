from django.urls import path
from .views import *

app_name = 'articles_app'

urlpatterns = [
    path('', index, name='index'),
    path('articles/<int:pk>/', view_article, name='view_article'),
]
