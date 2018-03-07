# -*- coding: utf-8 -*-
# coding=utf-8

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

import markdown
import config

extensions = config.MARKDOWN_EXTENSIONS

register = template.Library()

"""
这个mk暂时不用了,没有扩展，
现在用martor
https://github.com/agusmakmun/django-markdown-editor
"""


@register.filter(name='mk2html', is_safe=True)
@stringfilter
def mk2html(value):
    return mark_safe(
        markdown.markdown(value,
                          output_format='html5',
                          extensions=extensions,
                          safe_mode=True,
                          enable_attributes=False
                          )
    )
