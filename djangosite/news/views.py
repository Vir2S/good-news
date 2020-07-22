from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, ArticleSeries, ArticleCategory


def single_slug(request, single_slug):
    # first check to see if the url is in categories.

    categories = [a.category_slug for a in ArticleCategory.objects.all()]
    if single_slug in categories:
        matching_series = ArticleSeries.objects.filter(article_category__category_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Article.objects.filter(article_series__article_series=m.article_series).earliest("article_published")
            series_urls[m] = part_one.article_slug

        return render(request=request,
                      template_name='news/category.html',
                      context={"article_series": matching_series, "part_ones": series_urls})


def category(request):
    return render(request, 'news/categories.html', context={'categories': ArticleCategory.objects.all})


def news(request):
    return render(request, 'app/news.html')