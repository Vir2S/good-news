from django.contrib import admin
from .models import Article, ArticleSeries, ArticleCategory
from tinymce.widgets import TinyMCE
from django.db import models


class ArticleAdmin(admin.ModelAdmin):

    formfield_overrides = {
            models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30, 'font': 'normal'})},
            }


admin.site.register(ArticleSeries)
admin.site.register(ArticleCategory)
admin.site.register(Article)
