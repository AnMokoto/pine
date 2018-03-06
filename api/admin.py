# -*- coding: utf-8 -*-
# coding=utf-8
from django.contrib import admin

from .models.skill import (
    Skill, SkillGroup,
)
from .models.about import (
    About, Experience, Education, Product,
)

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
        self.message_user(request, "%s selected were successfully to set the display as show" % row_count)

    show_display.short_description = u'Show the selected articles'

    def hidden_display(self, request, queryset):
        row_count = queryset.update(display=False)
        self.message_user(request, "%s selected were successfully to set the display as hidden" % row_count)

    hidden_display.short_description = u'Hidden the selected articles'


class AdminSkillGroupInlines(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillGroup)
class AdminSkillGroup(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [AdminSkillGroupInlines]


@admin.register(Skill)
class AdminSkill(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'introduce', 'group_name')
    search_fields = ['name']
    list_filter = ['group']


class AdminAboutInfo(admin.ModelAdmin):
    # exclude = ['name']
    pass


@admin.register(About)
class AdminAbout(AdminAboutInfo):
    list_display = ('name', 'content', 'my_name', 'my_job', 'my_second', 'my_other', 'date',)
    empty_value_display = 'empty'


@admin.register(Experience)
class AdminExperience(AdminAboutInfo):
    list_display = ('company', 'office', 'start_date', 'end_date', 'content', 'date', 'display',)
    list_filter = ['start_date']
    search_fields = ['company']


@admin.register(Education)
class AdminEducation(AdminAboutInfo):
    list_display = ('school', 'start_date', 'end_date', 'content', 'date',)
    search_fields = ['school']
    ordering = ['-end_date']


@admin.register(Product)
class AdminProduct(AdminAboutInfo):
    list_display = ('product', 'thumbnail', 'content', 'display',)
    search_fields = ['product']


@admin.register(Article)
class AdminArticle(AdminDisplay):
    list_display = ('title', 'author', 'tips', 'numerous', 'calendar', 'update', 'display', 'group')
    list_filter = ['calendar', 'display', 'tips']
    ordering = ['-calendar', '-numerous', 'display', 'group']


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
