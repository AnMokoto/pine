# -*- coding: utf-8 -*-
# coding=utf-8
from django.urls import reverse
from django.contrib.sitemaps import Sitemap

from api.models.article import Article, ArticleGroup

"""
for sitemap with module `index`
"""


class __Sitemap(Sitemap):
    changefreq = 'weekly'


class _SitemapDetails(__Sitemap):
    def items(self):
        return Article.objects.all().filter(display=True)

    def location(self, obj):
        return reverse('home:details', args=[obj.pk])


class _SitemapArticles(__Sitemap):
    def items(self):
        return ArticleGroup.objects.all()

    def location(self, obj):
        return reverse('home:articles', args=[obj.pk])


sitemaps = {
    'details': _SitemapDetails,
    'articles': _SitemapArticles
}
