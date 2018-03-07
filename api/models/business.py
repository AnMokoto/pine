# -*- coding: utf-8 -*-
# coding=utf-8

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _


def article_desc(instance, filename):
    return "banner/{0}/{1}".format(instance.id, filename)


@python_2_unicode_compatible
class Banner(models.Model):
    """
    主页顶部封面
    """
    name = models.CharField(max_length=50, verbose_name=_(u"简介"), blank=True, null=True)
    desc = models.CharField(max_length=40, verbose_name=_(u"广告语"), blank=True, null=True)
    express = models.FileField(verbose_name=_(u"图片地址Local"), upload_to=article_desc, blank=True, null=True)
    url = models.URLField(verbose_name=_(u"图片地址remote"), blank=True, null=True)
    update = models.DateTimeField(verbose_name=_(u"更新时间"), editable=False, auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ADPP(models.Model):
    """
    广告商爸爸
    """
    name = models.CharField(max_length=50, verbose_name=u"简介", blank=True, null=True)
    desc = models.CharField(max_length=30, verbose_name=u"广告语", blank=True, null=True)
    url = models.URLField(verbose_name=u"图片地址", blank=True, null=True)
    update = models.DateTimeField(verbose_name=u"更新时间", editable=False, auto_now=True)
    target = models.URLField(verbose_name=u"跳转地址", blank=True, null=True)
    display = models.BooleanField(verbose_name=u"展示", default=False, )

    def __str__(self):
        return self.name
