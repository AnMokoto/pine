# -*- coding: utf-8 -*-
# coding=utf-8
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

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

    # article details
    url(r'^details/(?P<id>\d+)/$', views.articles.ArticleDetails, name='details'),

    url(r'^articles/$', views.articles.Articles, name='articles'),
    url(r'^articles/(?P<id>\d+)/$', views.articles.Articles, name='articles'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
