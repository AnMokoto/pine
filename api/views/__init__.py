# -*- coding: utf-8 -*-
# coding=utf-8

from django.shortcuts import render

from . import (
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
                  {'imagePath': business.Banner(request)})
