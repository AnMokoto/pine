# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models
from martor.widgets import AdminMartorWidget
from .models import (
    UserProfile,
)

admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


@admin.register(User)
class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline]

    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget}
    }

# class AdminSkillGroupInlines(admin.TabularInline):
#     model = Skill
#     extra = 1
#
#
# @admin.register(SkillGroup)
# class AdminSkillGroup(admin.ModelAdmin):
#     list_display = ('name',)
#     inlines = [AdminSkillGroupInlines]
#
#
# @admin.register(Skill)
# class AdminSkill(admin.ModelAdmin):
#     list_display = ('name', 'proficiency', 'introduce', 'group_name')
#     search_fields = ['name']
#     list_filter = ['group']
#
#
# class AdminAboutInfo(admin.ModelAdmin):
#     # exclude = ['name']
#     pass
#
#
# @admin.register(Experience)
# class AdminExperience(AdminAboutInfo):
#     list_display = ('company', 'office', 'start_date', 'end_date', 'content', 'date', 'display',)
#     list_filter = ['start_date']
#     search_fields = ['company']
#
#
# @admin.register(Education)
# class AdminEducation(AdminAboutInfo):
#     list_display = ('school', 'start_date', 'end_date', 'content', 'date',)
#     search_fields = ['school']
#     ordering = ['-end_date']
#
#
# @admin.register(Product)
# class AdminProduct(AdminAboutInfo):
#     list_display = ('product', 'thumbnail', 'content', 'display',)
#     search_fields = ['product']
