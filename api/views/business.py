# -*- coding: utf-8 -*-
# coding=utf-8
from api.models import business
from django.shortcuts import get_list_or_404, get_object_or_404


def Banner(request):
    banner = business.Banner.objects.all().order_by('-update').first()
    return banner


def ADpp(request):
    adpp = business.ADPP.objects.all().filter(display=True).order_by('-update')
    return list(adpp)
