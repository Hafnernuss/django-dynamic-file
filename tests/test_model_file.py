from django.test import TestCase
from django.apps import apps
from django.conf import settings

from dynamic_file.models import DynamicFile

import helpers
import base64

UploadedByModel = apps.get_model(settings.DYNAMIC_FILE_UPLOADED_BY_MODEL)


class DynamicFileModelTestCase(TestCase):

    def test_create_default(self):
        instance = DynamicFile.objects.create()

        assert instance.description == ''
        assert instance.uploaded_by is None
        instance.file.name == ''

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

    def test_read(self):
        instance = DynamicFile.objects.create(file=helpers.create_dummy_gif())
        assert instance.read == instance.file.read

    def test_mimetype(self):
        instance = DynamicFile.objects.create(file=helpers.create_dummy_gif('image.gif'))
        mimetype = instance.mimetype
        assert mimetype
        assert mimetype == 'image/gif'

    def test_to_base64(self):
        file = helpers.create_dummy_gif('image.gif')
        instance = DynamicFile.objects.create(file=file)

        assert base64.b64encode(helpers.SMALL_GIF) == instance.to_base64()

    def test_to_base64_utf8(self):
        file = helpers.create_dummy_gif('image.gif')
        instance = DynamicFile.objects.create(file=file)

        assert base64.b64encode(helpers.SMALL_GIF).decode('utf-8') == instance.to_base64_utf8()

    def test_to_base64_src(self):
        file = helpers.create_dummy_gif('image.gif')
        instance = DynamicFile.objects.create(file=file)

        b64 = base64.b64encode(helpers.SMALL_GIF).decode('utf-8')
        expected = f'data:;base64,{b64}'
        assert expected == instance.to_base64_src()

    def test_str(self):
        instance = DynamicFile.objects.create(file=None)
        assert str(instance.pk) in str(instance)

        instance = DynamicFile.objects.create(display_name='test')
        assert instance.display_name == str(instance)

        instance = DynamicFile.objects.create(file=helpers.create_dummy_gif('image.gif'))
        assert instance.name == str(instance)
