# -*- coding: utf-8 -*-
# coding=utf-8
from django.conf.urls import url

from index.views import articles

urlpatterns = [
    # article details
    url(r'^details/(?P<id>\d+)/$', articles.ArticleDetails, name='details'),

    url(r'^articles/$', articles.Articles, name='articles'),
    url(r'^articles/(?P<id>\d+)/$', articles.Articles, name='articles'),
]
