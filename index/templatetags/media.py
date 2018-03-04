# -*- coding: utf-8 -*-
# coding=utf-8
from django import template

register = template.Library()


@register.tag('media')
def do_media():
    pass
