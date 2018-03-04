from django.http import HttpResponse
from django.shortcuts import render
from api.views import about as api


def about(request, name='L'):
    info = request.GET.get("info", None)
    if str(info).__eq__(str(20180214)):
        return render(
            request,
            'about/index.html',
            {
                'title': str(name),
                'about': api.about(request),
                'skill': api.skill(request),
                'experience': api.experience(request),
                'product': api.product(request)
            }
        )
    else:
        return HttpResponse("What's wrong?")
