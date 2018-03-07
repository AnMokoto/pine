# -*- coding: utf-8 -*-
# coding=utf-8

from skill import (
    skill
)

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def get_user_by(*args, **kwargs):
    return get_object_or_404(User, *args, **kwargs)
