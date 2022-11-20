from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse


from rest_framework import serializers

from dynamic_file.models import DynamicFile
from dynamic_file.serializers import DynamicFileField


from test_app.models import TestModelOneToOne

import helpers


class TestModelOneToOneSerializer(serializers.Serializer):
    file = DynamicFileField()

    def get_file_url(self, dynamic_file):
        return reverse('serve_default', kwargs={'pk': dynamic_file.id})

    class Meta:
        model = TestModelOneToOne


class DynamicFileSerializerFieldTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.serializer = TestModelOneToOneSerializer

        cls.request = RequestFactory().get('', data={})

    def test_serialize_null(self):
        instance = TestModelOneToOne.objects.create()

        expected = {
            'file': None
        }

        actual = self.serializer(instance=instance, context={'request': self.request}).data

        assert expected == actual

    def test_serialize_valid_method(self):
        file = DynamicFile.objects.create(file=helpers.create_dummy_gif())
        instance = TestModelOneToOne.objects.create(file=file)

        expected = {
            'file': f'http://testserver/serve/{file.id}'
        }

        actual = self.serializer(instance=instance, context={'request': self.request}).data

        assert expected == actual
