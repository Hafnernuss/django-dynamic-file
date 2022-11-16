from django.db import models
from django.utils.translation import gettext as _
from dynamic_file.models.base import DynamicFileBase


class DynamicFile(DynamicFileBase):
    file = models.FileField(
        help_text=_('The uploaded file')
    )
