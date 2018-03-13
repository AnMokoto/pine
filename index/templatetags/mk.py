# -*- coding: utf-8 -*-
# coding=utf-8

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from martor.utils import markdownify
import markdown
import config

register = template.Library()


@register.filter(name=u"toc", is_safe=True)
@stringfilter
def mk2html(value):
    md = markdown.Markdown(extensions=config.MARKDOWN_EXTENSIONS)
    va = md.convert(value)
    return mark_safe(md.toc)
