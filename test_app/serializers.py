from rest_framework import serializers

from dynamic_file.serializers import DynamicFileField

from test_app.models import TestModelOneToOne


class TestModelOneToOneSerializer(serializers.Serializer):
    file = DynamicFileField()

    class Meta:
        model = TestModelOneToOne
