# -*- coding: utf-8 -*-
# coding=utf-8
from django.shortcuts import render, redirect
from django.urls import reverse

from api.views import articles, business


def ArticleDetails(request, id=1):
    article = articles.ArticleDetails(request, id)
    return render(request, "content/article/article-details.html", {
        'title': article.title,
        'article': article,
    })


def Articles(request, id=None):
    if id:
        art = articles.Articles(request, id)
        return render(request, 'content/article/articles.html', {
            'title': "",
            'articles': art,
            'article_group': articles.ArticlesGroup(request),
            'business': business.ADpp(request)
        })
    else:
        return ArticlesGroup(request)


def ArticlesGroup(request):
    return redirect(reverse('home:home', ))
