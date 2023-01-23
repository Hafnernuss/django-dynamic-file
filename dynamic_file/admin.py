from django.contrib import admin

from .models import DynamicFile


@admin.register(DynamicFile)
class CourseGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
