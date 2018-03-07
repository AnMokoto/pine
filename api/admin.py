# -*- coding: utf-8 -*-
# coding=utf-8
from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from django.utils.translation import ugettext_lazy as _

from .models.article import (
    Article, ArticleGroup
)

from .models import business


class AdminDisplay(admin.ModelAdmin):
    """
    增加action控制多选的显示和隐藏
    """
    actions = ['show_display', 'hidden_display', ]

    def show_display(self, request, queryset):
        row_count = queryset.update(display=True)
        self.message_user(request, _("%s selected were successfully to set the display as show") % row_count)

    show_display.short_description = _(u'Show the selected articles')

    def hidden_display(self, request, queryset):
        row_count = queryset.update(display=False)
        self.message_user(request, _("%s selected were successfully to set the display as hidden") % row_count)

    hidden_display.short_description = _(u'Hidden the selected articles')


@admin.register(Article)
class AdminArticle(AdminDisplay):
    list_display = ('title', 'author', 'tips', 'numerous', 'calendar', 'update', 'display', 'group')
    list_filter = ['calendar', 'display', 'tips']
    ordering = ['-calendar', '-numerous', 'display', 'group']
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


@admin.register(ArticleGroup)
class AdminArticleGroup(admin.ModelAdmin):
    list_display = ['name']


@admin.register(business.Banner)
class BusinessBanner(admin.ModelAdmin):
    list_display = ('name', 'express', 'url', 'desc', 'update')
    ordering = ['-update']
    list_filter = ['update']
    search_fields = ['name', 'url']


@admin.register(business.ADPP)
class BusinessADPP(AdminDisplay):
    list_display = ('name', 'url', 'target', 'desc', 'update', 'display')
    ordering = ['-update']
    list_filter = ['update']
    search_fields = ['name', 'url']
