from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

from dynamic_file.models.base import DynamicFileBase

class DynamicFile(DynamicFileBase):
    file = models.FileField(
        storage=settings.DYNAMIC_FILE_STORAGE_CLASS,
        help_text=_('The uploaded file')
    )