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

    @property
    def name(self):
        return self.file.name

    def __str__(self):
        '''
        String representation of this model. Defaults to the name of the file.
        If no file has been set, returnes the pk with a fixed suffix.
        '''
        return self.file.name if self.file.name else f'{self.pk}_nofile'
