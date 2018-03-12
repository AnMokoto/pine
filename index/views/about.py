from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from users import views as users
from django.shortcuts import get_object_or_404


def about(request, name=None):
    author = users.get_user_by(Q(username=name) | Q(email=name))
    lang = request.GET.get("lang", None)

    return render(request,
                  'about/index.html',
                  {
                      'title': str(name),
                      'author': author,
                      'lang': str(lang),
                      'local': 'zh'
                  })
