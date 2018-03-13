# -*- coding: utf-8 -*-
# coding=utf-8
from django.shortcuts import get_object_or_404, get_list_or_404

from api.models.article import Article, ArticleGroup


def ArticleDetails(request, id=1):
    article = get_object_or_404(Article, pk=id)
    if article and article.display:
        article.increase_views()  # 增加阅读数
    return article


def Articles(request, id=None):
    obj = Article.objects.all().order_by("-calendar")
    if id:
        obj = obj.filter(group__id=id)
    e = list(obj.distinct())
    return e


def ArticlesGroup(request):
    group = get_list_or_404(ArticleGroup)
    return group
