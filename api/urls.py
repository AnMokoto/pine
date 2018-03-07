# -*- coding: utf-8 -*-
# coding=utf-8

from django.conf.urls import url

import api.views as views

app_name = 'api'

urlpatterns = [
    # 默认接口主页
    url(r'^$', views.index, name='index'),
]
