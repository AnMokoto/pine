# -*- coding: utf-8 -*-
# coding=utf-8

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

extensions = ['markdown.extensions.toc', 'tables',
              WikiLinkExtension(base_url='https://en.wikipedia.org/wiki/',
                                end_url='#Hyperlinks_in_wikis'),
              'markdown.extensions.sane_lists',
              # 'markdown.extensions.abbr',
              # 'markdown.extensions.attr_list',
              # 'markdown.extensions.def_list',
              # 'markdown.extensions.fenced_code',
              # 'markdown.extensions.footnotes',
              # 'markdown.extensions.smart_strong',
              'markdown.extensions.meta',
              'markdown.extensions.nl2br',
              'markdown.extensions.codehilite',
              'markdown.extensions.extra',
              'markdown.extensions.sane_lists',
              'markdown.extensions.smarty',
              'markdown.extensions.tables'
              ]

register = template.Library()


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
