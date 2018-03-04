from . import (
    index,
    about,
    articles,
)

from django.shortcuts import render

from api.views import articles as art
from api.views import business


def home(request):
    return render(request,
                  'content/home.html',
                  {'title': u"home",
                   'articles': art.Articles(request),
                   'article_group': art.ArticlesGroup(request),
                   'business_banner': business.Banner(request),
                   'business_adpp': business.ADpp(request)
                   }
                  )


def test(request):
    return render(request, 'content/article/article-details.html', {'title': u"detail"})
