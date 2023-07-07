from django.db import models
from django.utils.translation import gettext as _
from dynamic_file.models.base import DynamicFileBase
from dynamic_file.storage import DynamicFileSystemStorage


fs = DynamicFileSystemStorage()


class DynamicFile(DynamicFileBase):
    file = models.FileField(
        storage=fs,
        help_text=_('The uploaded file')
    )
    '''
    The concrete file for this model.
    '''
