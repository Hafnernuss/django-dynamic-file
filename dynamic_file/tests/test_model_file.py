from django.test import TestCase

from dynamic_file.models import DynamicFile


class DynamicFileModelTestCase(TestCase):

    def test_create_default(self):
        model = DynamicFile.objects.create()

        assert model.description == ''
        assert model.uploaded_by is None
