# -*- coding: utf-8 -*-
# coding=utf-8

from django.conf.urls import url

import views
app_name = 'user'

urlpatterns = [
    url(r'^skill/$',views.skill, name='skill'),
    url(r'^skill/(?P<name>\w+)/$', views.skill, name='skill'),
]
