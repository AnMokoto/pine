# -*- coding: utf-8 -*-
# coding=utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.


@python_2_unicode_compatible
class SkillGroup( models.Model, ):
    """
    技能表述
    @name 技能名（总类）
    """
    name = models.TextField(max_length=20, verbose_name=u"类型")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Skill( models.Model, ):
    """
    技能表述
    @name 技能名（explain：js,es6,ts,vue,...）
    @proficiency 技能熟练度
    @introduce 技能描述页面
    """
    name = models.TextField(verbose_name=u"技能")
    proficiency = models.IntegerField(null=False, verbose_name=u"熟练度")
    introduce = models.TextField(blank=True, null=True, verbose_name=u"详情")
    group = models.ForeignKey(SkillGroup, on_delete=models.CASCADE)

    # @property
    def group_name(self):
        return self.group.name

    def __str__(self):
        return self.name
