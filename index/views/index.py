from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index/index.html', {'title': 'index'})


def error(request):
    return render(request, 'error.html')


def info(request, name=None):
    if not name:
        string = "OK"
    else:
        string = str(name)
    return HttpResponse(string)
