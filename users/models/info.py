# # -*- coding: utf-8 -*-
# # coding=utf-8
# from django.contrib.auth.models import User
# from django.db import models
# from django.db.models.signals import post_save
# from django.utils.encoding import python_2_unicode_compatible
# import sys
#
#
# @python_2_unicode_compatible
# class AboutInfo(models.Model, ):
#     name = models.CharField(max_length=10, verbose_name=u"类型", editable=False)
#     date = models.DateTimeField(verbose_name=u"最后更新", auto_now=True, )
#     display = models.BooleanField(verbose_name=u"展示", default=False)  # visibility
#
#     @property
#     def name(self):
#         return self.__str__()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         abstract = True
#
#
# @python_2_unicode_compatible
# class Experience(AboutInfo):
#     user = models.ForeignKey(User)
#     company = models.CharField(verbose_name=u"公司名", max_length=50, )
#     office = models.CharField(verbose_name=u"职位", max_length=50, )
#     start_date = models.DateField(verbose_name=u"开始时间", editable=True, )
#     end_date = models.DateField(verbose_name=u"结束时间", editable=True, null=True, blank=True)
#     content = models.CharField(verbose_name=u"内容", max_length=sys.maxsize, )
#
#     def __str__(self):
#         return u"经历"
#
#     class Meta:
#         # db_table = 'about_experience'
#         get_latest_by = 'start_date'
#         ordering = ['-start_date']
#
#
# def create_user_experience(sender, instance, created, **kwargs):
#     if created:
#         profile = Experience()
#         profile.user = instance
#         profile.save()
#
#
# post_save.connect(create_user_experience, sender=User)
#
#
# @python_2_unicode_compatible
# class Education(AboutInfo):
#     user = models.ForeignKey(User)
#     school = models.CharField(verbose_name=u"学校", max_length=50, )
#     start_date = models.DateField(verbose_name=u"开始时间", editable=True, )
#     end_date = models.DateField(verbose_name=u"结束时间", editable=True, null=True)
#     content = models.CharField(verbose_name=u"详情", max_length=sys.maxsize)
#
#     def __str__(self):
#         return u"教育"
#
#     # class Meta:
#     # db_table = 'about_education'
#
#
# def create_user_education(sender, instance, created, **kwargs):
#     if created:
#         profile = Experience()
#         profile.user = instance
#         profile.save()
#
#
# post_save.connect(create_user_education, sender=User)
#
#
# @python_2_unicode_compatible
# class Product(AboutInfo):
#     user = models.ForeignKey(User)
#     product = models.CharField(verbose_name=u"产品", max_length=50, )
#     thumbnail = models.URLField(verbose_name=u"图片", )
#     content = models.CharField(verbose_name=u"详情", max_length=sys.maxsize)
#
#     def __str__(self):
#         return u"产品"
#
#     # class Meta:
#     #     db_table = 'about_product'
#
#
# def create_user_produce(sender, instance, created, **kwargs):
#     if created:
#         profile = Product()
#         profile.user = instance
#         profile.save()
#
#
# post_save.connect(create_user_produce, sender=User)
