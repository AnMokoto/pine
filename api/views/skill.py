from django.http.response import HttpResponse
from django.http.request import QueryDict
import json

from api.models.skill import SkillGroup, Skill


# Create your views here.
def skill(request, name=None):
    if not name:
        response = json.dumps(skill_group())
    else:
        response = json.dumps(__skill(name))
    return HttpResponse(response)


def __skill(name=None):
    """
    :param name: group name
    :return: skill in group
    """
    group = SkillGroup.objects.filter(name=name).all().distinct()
    data = Skill.objects.filter(group=group).distinct().values('name', 'proficiency', 'introduce', 'group__name')
    return list(data)


def skill_group():
    group = SkillGroup.objects.all().distinct()
    if group and group.exists():
        query_dict = QueryDict(mutable=True)
        for v in group:
            name = v.name
            data = __skill(name)
            query_dict.appendlist(name, data)
        return query_dict
    else:
        return str("Not Found.")
