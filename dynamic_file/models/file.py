from django.db import models
from django.utils.translation import gettext as _
from dynamic_file.models.base import DynamicFileBase


class DynamicFile(DynamicFileBase):
    file = models.FileField(
        help_text=_('The uploaded file')
    )
    '''
    The concrete file for this model.
    '''

    def __str__(self):
        '''
        String representation of this model. Defaults to the name of the file.
        If no file has been set, returnes the pk with a fixed suffix.
        '''
        return self.file.name if self.file.name else f'{self.pk}_nofile'
