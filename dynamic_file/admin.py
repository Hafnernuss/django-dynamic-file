from django.contrib import admin

from .models import DynamicFile
from django.utils.safestring import mark_safe


def preview(dynamic_file):
    mimetype = dynamic_file.mimetype
    if mimetype and 'image' in mimetype:
        src = dynamic_file.to_base64_src()
        return mark_safe(f'<img src="{src}" width="150" />')
    else:
        return 'No preview available'


@admin.register(DynamicFile)
class DynamicFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['preview']

    def preview(self, instance):
        return preview(instance)
