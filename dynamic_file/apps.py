from django.apps import AppConfig
from dynamic_file import config


class DynamicFileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dynamic_file'
