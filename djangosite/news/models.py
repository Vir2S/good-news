from django.db import models
from tinymce.models import HTMLField
from datetime import datetime


class ArticleCategory(models.Model):
    article_category = models.CharField(max_length=100)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.article_category


class ArticleSeries(models.Model):
    article_series = models.CharField(max_length=200)
    article_category = models.ForeignKey(ArticleCategory, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.article_series


class Article(models.Model):
    title = models.CharField('Title', max_length=160)
    date = models.DateTimeField('Publication date', default=datetime.now())
    short_story = models.TextField('Short story', max_length=300)
    full_story = HTMLField('Full story')

    article_series = models.ForeignKey(ArticleSeries, default=1, verbose_name='Series', on_delete=models.SET_DEFAULT)
    article_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.title
