# -*- coding: utf-8 -*-
# coding=utf-8
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from index import views, sitemaps

import articles

app_name = 'home'

urlpatterns = [
    url(r'^test$', views.test, name='home'),
    # 默认主页
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.index.index, name='index'),
    # 关于
    url(r'^about/(?P<name>\w+)/$', views.about.about, name='about'),

    # 详情
    url(r'^info/$', views.index.info, name='info'),
    url(r'^info/(?P<name>.+)/$', views.index.info, name='info'),

    # sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps.sitemaps},
        name='django.contrib.sitemaps.views.sitemap')

]
# articles
urlpatterns += articles.urlpatterns
