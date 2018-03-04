# -*- coding: utf-8 -*-
# coding=utf-8

from django.shortcuts import render

from . import (
    about,
    skill,
    articles,
    business,
)

"""
处理数据,不做ui处理
"""


def index(request):
    """
    :param request:
    :return: 默认接口主页
    """
    return render(request, 'api/index.html',
                  {'imagePath': '/static/images/desktop/8bb75851eb1532b19b56e8ac9aaf1ca9.jpg'})
