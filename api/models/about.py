# -*- coding: utf-8 -*-
# coding=utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import sys


@python_2_unicode_compatible
class AboutInfo(models.Model, ):
    name = models.TextField(verbose_name=u"类型", editable=False)
    date = models.DateTimeField(verbose_name=u"最后更新", auto_now=True, )

    @property
    def name(self):
        return self.__str__()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


@python_2_unicode_compatible
class About(AboutInfo):
    content = models.TextField(verbose_name=u"内容", max_length=sys.maxsize, )
    my_name = models.TextField(verbose_name=u"姓名", default=u"保密")
    my_job = models.TextField(verbose_name=u"工作类型", default=u"保密")
    my_second = models.TextField(verbose_name=u"座右铭", blank=True)
    my_other = models.TextField(verbose_name=u"其他信息", blank=True)

    def __str__(self):
        return u"关于我"

    class Meta:
        db_table = 'about_info'


@python_2_unicode_compatible
class Experience(AboutInfo):
    content = models.TextField(verbose_name=u"内容", max_length=sys.maxsize, )
    start_date = models.DateField(verbose_name=u"开始时间", editable=True, )
    end_date = models.DateField(verbose_name=u"结束时间", editable=True, null=True, blank=True)
    office = models.TextField(verbose_name=u"职位", max_length=50, )
    company = models.TextField(verbose_name=u"公司名", max_length=50, )
    display = models.BooleanField(verbose_name=u"展示", default=True)  # visibility

    def __str__(self):
        return u"经历"

    class Meta:
        db_table = 'about_experience'
        get_latest_by = 'start_date'
        ordering = ['-start_date']


@python_2_unicode_compatible
class Education(AboutInfo):
    school = models.TextField(verbose_name=u"学校", max_length=50, )
    start_date = models.DateField(verbose_name=u"开始时间", editable=True, )
    end_date = models.DateField(verbose_name=u"结束时间", editable=True, null=True)
    content = models.TextField(verbose_name=u"详情")

    def __str__(self):
        return u"教育"

    class Meta:
        db_table = 'about_education'


@python_2_unicode_compatible
class Product(AboutInfo):
    product = models.TextField(verbose_name=u"产品", max_length=50, )
    thumbnail = models.URLField(verbose_name=u"图片", )
    content = models.TextField(verbose_name=u"详情", )
    display = models.BooleanField(verbose_name=u"展示", default=True, )

    def __str__(self):
        return u"产品"

    class Meta:
        db_table = 'about_product'
