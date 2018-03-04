from django.test import TestCase
from .models import SkillGroup, Skill
import json


# Create your tests here.
class SkillGroupTest(TestCase):

    def test_create_skill_group(self):
        """
        test for skill
        """
        js = 'python'

        group = SkillGroup(name=js, )
        group.save()

        jscript = Skill(name='python', proficiency=80, introduce='info/python', group=group)
        jscript.save()

        es6 = Skill(name='django', proficiency=80, introduce='info/django', group=group)
        es6.save()
        #
        # vue = Skill(name='vue', proficiency=40, introduce='info/vue', group=group)
        # vue.save()
