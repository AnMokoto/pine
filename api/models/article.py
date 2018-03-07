# -*- coding: utf-8 -*-
# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import sys

from martor.models import MartorField


def article_desc(instance, filename):
    return "article/{0}/{1}".format(instance.id, filename)


@python_2_unicode_compatible
class ArticleGroup(models.Model):
    name = models.CharField(verbose_name=u"文章类型", max_length=20)
    express = models.FileField(upload_to=article_desc, blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Article(models.Model):
    tips = models.CharField(verbose_name=u"声明", max_length=10, editable=True, blank=True, null=True, default=u"Develop")
    # author = models.TextField(verbose_name=u"作者", blank=True, null=True, editable=True, default=u"佚名")
    author = models.ForeignKey(User, verbose_name=u"作者", on_delete=models.DO_NOTHING, )
    title = models.CharField(verbose_name=u"标题", max_length=25, blank=False, null=False, )

    calendar = models.DateField(verbose_name=u"发布时间", auto_now_add=True)
    update = models.DateTimeField(verbose_name=u"最后更新", auto_now=True)
    numerous = models.IntegerField(verbose_name=u"点击数量", editable=True, blank=True, default=100)
    display = models.BooleanField(verbose_name=u"展示", default=True, )
    group = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE, verbose_name=u"文章类型")
    # 采用markdown存储
    # thumbnail = models.URLField(verbose_name=u"缩略图")
    thumbnail_content = MartorField(verbose_name=u"缩略文字", blank=True, max_length=300)
    content = MartorField(verbose_name=u"内容详情", blank=True, max_length=sys.maxsize)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    # return const.get_absolute_url('api:details', args=[self.id])

    def group_name(self):
        return self.group.__str__()
