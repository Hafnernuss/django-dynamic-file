from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework import serializers

from dynamic_file.models import DynamicFile
from dynamic_file.serializers import DynamicFileField

from test_app.models import TestModelOneToOne

import helpers


class ModelOneToOneSerializer(serializers.ModelSerializer):
    file = DynamicFileField(allow_null=True)

    def get_file_url(self, dynamic_file):
        return reverse('serve_default', kwargs={'pk': dynamic_file.id})

    class Meta:
        model = TestModelOneToOne
        fields = ['file']


class ModelOneToOneSerializerWithFallback(serializers.ModelSerializer):
    file = DynamicFileField()

    def get_file_fallback_url(self, instance):
        return instance.id  # just to mock something unique

    class Meta:
        model = TestModelOneToOne
        fields = ['file']


class DynamicFileSerializerFieldTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.request = RequestFactory().get('', data={})

    def test_serialize_null(self):
        instance = TestModelOneToOne.objects.create()

        expected = {'file': None}
        actual = ModelOneToOneSerializer(instance=instance, context={'request': self.request}).data

        assert expected == actual

    def test_serialize_null_fallback(self):
        instance = TestModelOneToOne.objects.create()

        expected = {'file': instance.pk}
        actual = ModelOneToOneSerializerWithFallback(instance=instance, context={'request': self.request}).data

        assert expected == actual

    def test_serialize(self):
        file = DynamicFile.objects.create(file=helpers.create_dummy_gif())
        instance = TestModelOneToOne.objects.create(file=file)

        expected = {'file': f'http://testserver/serve/{file.id}'}
        actual = ModelOneToOneSerializer(instance=instance, context={'request': self.request}).data

        assert expected == actual

    def test_serialize_no_request(self):
        file = DynamicFile.objects.create(file=helpers.create_dummy_gif())
        instance = TestModelOneToOne.objects.create(file=file)

        expected = {'file': f'/serve/{file.id}'}
        actual = ModelOneToOneSerializer(instance=instance).data

        assert expected == actual

    def test_create(self):
        payload = {'file': helpers.create_dummy_gif()}
        serializer = ModelOneToOneSerializer(data=payload)
        assert serializer.is_valid()
        instance = serializer.save()

        assert instance.file
        assert instance.file.file.read() == helpers.create_dummy_gif().read()
        assert DynamicFile.objects.count() == 1

    def test_create_empty(self):
        payload = {'file': None}
        serializer = ModelOneToOneSerializer(data=payload)
        assert serializer.is_valid()
        instance = serializer.save()

        assert instance.file is None
        assert DynamicFile.objects.count() == 0

    def test_update(self):
        file = DynamicFile.objects.create(file=helpers.create_dummy_gif())
        instance = TestModelOneToOne.objects.create(file=file)

        payload = {'file': SimpleUploadedFile('anotherfile.txt', b'some_content')}
        serializer = ModelOneToOneSerializer(instance=instance, data=payload)
        assert serializer.is_valid()

        instance = serializer.save()
        assert instance.file.file.read() == b'some_content'
        assert DynamicFile.objects.count() == 1

    def test_delete(self):
        file = DynamicFile.objects.create(file=helpers.create_dummy_gif())
        instance = TestModelOneToOne.objects.create(file=file)

        payload = {'file': None}
        serializer = ModelOneToOneSerializer(instance=instance, data=payload)
        assert serializer.is_valid()

        instance = serializer.save()
        assert instance.file is None
        assert DynamicFile.objects.count() == 0
