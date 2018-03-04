# -*- coding: utf-8 -*-
# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import sys


def article_desc(instance, filename):
    return "article/{0}/{1}".format(instance.id, filename)


@python_2_unicode_compatible
class ArticleGroup(models.Model):
    name = models.TextField(verbose_name=u"文章类型", max_length=20)
    express = models.FileField(upload_to=article_desc, blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Article(models.Model):
    tips = models.TextField(verbose_name=u"声明", editable=True, blank=True, null=True, default=u"Develop")
    # author = models.TextField(verbose_name=u"作者", blank=True, null=True, editable=True, default=u"佚名")
    author = models.ForeignKey(User, verbose_name=u"作者", on_delete=models.DO_NOTHING)
    title = models.TextField(verbose_name=u"标题", blank=False, null=False, max_length=30)

    calendar = models.DateField(verbose_name=u"发布时间", auto_now_add=True)
    update = models.DateTimeField(verbose_name=u"最后更新", auto_now=True)
    numerous = models.IntegerField(verbose_name=u"点击数量", editable=True, blank=True, default=100)
    display = models.BooleanField(verbose_name=u"展示", default=True)
    # 采用markdown存储
    thumbnail_content = models.TextField(verbose_name=u"缩略文字", blank=True, max_length=300)
    # thumbnail = models.URLField(verbose_name=u"缩略图")
    content = models.TextField(verbose_name=u"内容详情", max_length=sys.maxint, blank=True)
    group = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE, verbose_name=u"文章类型")

    def __str__(self):
        return self.title

    def group_name(self):
        return self.group.__str__()
