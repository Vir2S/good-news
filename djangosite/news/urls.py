from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Article, ArticleCategory
from . import views


app_name = 'news'

urlpatterns = [
    path('',
         ListView.as_view(queryset=Article.objects.all().order_by('-date')[:20],
                          template_name='news/posts.html')),
    path('<int:pk>/',
         DetailView.as_view(model=Article,
                            template_name='news/post.html')),
    path('categories/',
         ListView.as_view(queryset=ArticleCategory.objects.all()[:20],
                          template_name='news/categories.html')),
    path('<single_slug>/', views.single_slug, name='single_slug'),
]
