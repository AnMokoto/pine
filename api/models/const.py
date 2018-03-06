# -*- coding: utf-8 -*-
# coding=utf-8
from django.urls import reverse

"""
公共models 配置参数项
"""

STATIC_CHOICES = (
    (True, 'show'),
    (False, 'hidden')
)


def get_absolute_url(space, *args, **kwargs):
    return reverse(space, args, kwargs)
