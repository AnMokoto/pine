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
class AdminArticle(admin.ModelAdmin):
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
class BusinessADPP(admin.ModelAdmin):
    list_display = ('name', 'url', 'target', 'desc', 'update', 'display')
    ordering = ['-update']
    list_filter = ['update']
    search_fields = ['name', 'url']
