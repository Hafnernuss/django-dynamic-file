from django.test import TestCase
from django.apps import apps
from django.conf import settings

from dynamic_file.models import DynamicFile

import helpers

UploadedByModel = apps.get_model(settings.DYNAMIC_FILE_UPLOADED_BY_MODEL)


class DynamicFileModelTestCase(TestCase):

    def test_create_default(self):
        instance = DynamicFile.objects.create()

        assert instance.description == ''
        assert instance.uploaded_by is None
        instance.file.name == ''

    def test_reverse_accessor(self):
        uploader = UploadedByModel.objects.create()
        instance = DynamicFile.objects.create(uploaded_by=uploader)

        assert instance in getattr(uploader, settings.DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME).all()

    def test_description(self):
        desc = 'A sample description for this file'
        instance = DynamicFile.objects.create(description=desc)

        assert instance.description == desc

    def test_name(self):
        instance = DynamicFile.objects.create(file=helpers.create_dummy_gif())

        assert instance.name == instance.file.name

    def test_storage_location(self):
        instance = DynamicFile.objects.create(file=helpers.create_dummy_gif())

        assert instance.file.name != ''
        assert instance.file.read() == helpers.create_dummy_gif().read()
