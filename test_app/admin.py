from django.contrib import admin

from test_app.models import TestModelOneToOne
from test_app.models import TestModel

from dynamic_file.admin import preview as image_preview


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    pass


@admin.register(TestModelOneToOne)
class TestModelOneToOneAdmin(admin.ModelAdmin):
    fields = ['file', 'preview']
    readonly_fields = ['preview']

    def preview(self, instance):
        return image_preview(instance.file)
