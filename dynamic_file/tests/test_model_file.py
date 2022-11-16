from django.test import TestCase
from django.apps import apps
from django.conf import settings

from dynamic_file.models import DynamicFile

UploadedByModel = apps.get_model(settings.DYNAMIC_FILE_UPLOADED_BY_MODEL)


class DynamicFileModelTestCase(TestCase):

    def test_create_default(self):
        model = DynamicFile.objects.create()

        assert model.description == ''
        assert model.uploaded_by is None
        model.file.name == ''

    def test_reverse_accessor(self):
        uploader = UploadedByModel.objects.create()

        model = DynamicFile.objects.create(uploaded_by=uploader)
        print(uploader.files_uploaded.all()[0])
        print( model in uploader.files_uploaded.all())
