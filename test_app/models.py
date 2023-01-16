from django.db import models
from dynamic_file.models import DynamicFile


class TestModel(models.Model):
    name = models.CharField(
        max_length=28,
        blank=True
    )


class TestModelOneToOne(models.Model):
    file = models.OneToOneField(
        DynamicFile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='one_to_one_file'
    )
