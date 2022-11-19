from django.test import TestCase
from django.apps import apps
from django.conf import settings
from django.urls import reverse

from django.test import TestCase, override_settings

from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from dynamic_file.models import DynamicFile
from dynamic_file.views import ServeDynamicFile

import helpers


class ServeDynamicFileTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.view_name = 'serve_default'
        cls.instance_1 = DynamicFile.objects.create(file=helpers.create_dummy_gif())

    @override_settings
    def test_serve_content_debug(self):
        factory = APIRequestFactory()
        request = factory.get('')

        view = ServeDynamicFile.as_view()
        response = view(request, pk=self.instance_1.pk)

        #  client = APIClient()
        #  r = client.get(reverse(self.view_name, kwargs={'pk': self.instance_1.id}))
        #  #response = view(request)



