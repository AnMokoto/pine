from api.models.about import (
    About,
    Experience,
    Product,
)

from .skill import skill_group


def about(request):
    a = About.objects.all()
    return a.last()


def experience(request):
    e = Experience.objects.all().distinct()
    return list(e)


def product(request):
    e = Product.objects.all().distinct()
    return list(e)


def skill(request):
    # return json.dumps(skill_group())
    return skill_group()._iteritems()
