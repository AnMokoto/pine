"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json, os
from django.utils.translation import ugettext_lazy as _

from index.views import index

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.conf.urls.static import static


@login_required
def markdown_uploader(request):
    """
       Makdown image upload for uploading to imgur.com
       and represent as json to markdown editor.
       """
    try:
        if request.method == 'POST' and request.is_ajax():
            if 'markdown-image-upload' in request.FILES:
                image = request.FILES['markdown-image-upload']
                local = 'markdown/%s' % image.name
                default_storage.save(os.path.join(settings.MEDIA_ROOT, local),
                                     ContentFile(image.read()))
                return HttpResponse(json.dumps({
                    'status': 200,
                    'link': os.path.join(settings.MEDIA_URL, local),
                    'name': image.name
                }), content_type='application/json')
    except Exception as e:
        print(e)
    return HttpResponse(_('Invalid request!'))


urlpatterns = [
    url(r'^api/', include('api.urls', namespace='my-api')),
    url(r'', include('index.urls', namespace='my-home')),
    url(r'^admin/', admin.site.urls),
    url(r'^martor/uploader/$', markdown_uploader, name='imgur_uploader'),
    url(r'^martor/', include('martor.urls'), ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = index.error
handler403 = index.error
