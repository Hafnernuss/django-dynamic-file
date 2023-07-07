
from django.test import TestCase

from dynamic_file.models import DynamicFile
from dynamic_file.admin import preview
import helpers


class AdminTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.instance_1 = DynamicFile.objects.create(file=helpers.create_dummy_gif())
        cls.instance_2 = DynamicFile.objects.create(file=helpers.create_dummy_gif('not_a_gif.exe'))

    def test_preview(self):
        response = preview(self.instance_1)
        assert '<img' in response

    def test_preview_no_image(self):
        response = preview(self.instance_2)
        assert '<img' not in response
