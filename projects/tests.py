from django.test import TestCase
from django import setup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProjectCaster.settings")
setup()

from .models import Project

class ProjectTestCase(TestCase):
    def test_queryset_exists(self):
        queries = Project.objects.all()
        self.assertTrue(queries.exists())