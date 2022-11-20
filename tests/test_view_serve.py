from django.http import FileResponse
from django.http import HttpResponse
from django.test import TestCase
from django.apps import apps
from django.conf import settings
from django.urls import reverse

from django.test import TestCase, override_settings

from rest_framework.test import APIRequestFactory
from rest_framework import status

from dynamic_file.models import DynamicFile
from dynamic_file.views import ServeDynamicFile

import os

import helpers


class ServeDynamicFileTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.view_name = 'serve_default'
        cls.instance_1 = DynamicFile.objects.create(file=helpers.create_dummy_gif())

    @override_settings(DEBUG=True)
    def test_serve_content_debug(self):
        factory = APIRequestFactory()
        request = factory.get('')

        view = ServeDynamicFile.as_view()
        response = view(request, pk=self.instance_1.pk)

        assert response.status_code is status.HTTP_200_OK
        assert isinstance(response, FileResponse)
        assert response.filename == self.instance_1.file.name

    def test_serve_content_production(self):
        factory = APIRequestFactory()
        request = factory.get('')

        view = ServeDynamicFile.as_view()
        response = view(request, pk=self.instance_1.pk)

        assert response.status_code is status.HTTP_200_OK
        assert isinstance(response, HttpResponse)
        assert 'X-Accel-Redirect' in response.headers.keys()
        assert 'Content-Type' in response.headers.keys()
        assert 'Content-Disposition' in response.headers.keys()
        assert 'Content-Encoding' in response.headers.keys()

        assert response.headers['X-Accel-Redirect'] == os.path.join(settings.DYNAMIC_FILE_STORAGE_LOCATION, self.instance_1.file.name)
