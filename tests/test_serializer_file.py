from django.test import TestCase
from django.apps import apps
# from django.conf import settings

from test_app.models import TestModelOneToOne
from test_app.serializers import TestModelOneToOneSerializer

# import helpers


class DynamicFileSerializerFieldTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.serializer = TestModelOneToOneSerializer

    def test_null(self):
        instance = TestModelOneToOne.objects.create()

        expected = {
            'file': None
        }

        actual = self.serializer(instance=instance).data

        assert expected == actual
