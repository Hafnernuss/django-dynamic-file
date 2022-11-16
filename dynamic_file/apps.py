from django.apps import AppConfig

from dynamic_file import config

config.settings


class DynamicFileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dynamic_file'
