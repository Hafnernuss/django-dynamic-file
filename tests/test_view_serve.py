from django.http import FileResponse
from django.http import HttpResponse
from django.test import TestCase
from django.test import override_settings
from django.conf import settings

from rest_framework.test import APIRequestFactory
from rest_framework import status

from dynamic_file.models import DynamicFile
from dynamic_file.views import ServeDynamicFile

from test_app.views import ServeTestFile

import os

import helpers


class ServeDynamicFileTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.view = ServeDynamicFile.as_view()
        cls.instance_1 = DynamicFile.objects.create(file=helpers.create_dummy_gif())

    @override_settings(DEBUG=True)
    def test_serve_content_debug(self):
        factory = APIRequestFactory()
        request = factory.get('')

        response = self.view(request, pk=self.instance_1.pk)

        assert response.status_code is status.HTTP_200_OK
        assert isinstance(response, FileResponse)
        assert response.filename == self.instance_1.file.name

    def test_serve_content_production(self):
        factory = APIRequestFactory()
        request = factory.get('')

        response = self.view(request, pk=self.instance_1.pk)
        expected_path = os.path.join(settings.DYNAMIC_FILE_STORAGE_LOCATION, self.instance_1.file.name)

        assert response.status_code is status.HTTP_200_OK
        assert isinstance(response, HttpResponse)
        assert 'X-Accel-Redirect' in response.headers.keys()
        assert 'Content-Type' in response.headers.keys()
        assert 'Content-Disposition' in response.headers.keys()
        assert 'Content-Encoding' in response.headers.keys()
        assert response.headers['X-Accel-Redirect'] == expected_path

        with open(response.headers['X-Accel-Redirect'], 'rb') as file:
            assert file.read() == self.instance_1.file.read()


class ServeCustomDynamicFileTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.view = ServeTestFile.as_view()
        cls.instance_1 = DynamicFile.objects.create(file=helpers.create_dummy_gif())

    @override_settings(DEBUG=True)
    def test_serve_content(self):
        factory = APIRequestFactory()
        request = factory.get('')

        response = self.view(request, key=self.instance_1.pk)

        assert response.status_code is status.HTTP_200_OK
        assert isinstance(response, FileResponse)
        assert response.filename == self.instance_1.file.name
