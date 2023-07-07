from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
import mimetypes

import base64


class DynamicFileBase(models.Model):
    '''
    Base model for handling dynamic files. Abstract, cannot be used directly.
    '''

    display_name = models.CharField(
        blank=True,
        default='',
        max_length=128,
        help_text=_('An optional displayable name for this file.')
    )
    '''
    A concise and optional description of the uploaded file.
    '''

    description = models.TextField(
        blank=True,
        help_text=_('A description for this file')
    )
    '''
    A concise and optional description of the uploaded file.
    '''

    uploaded_by = models.ForeignKey(
        settings.DYNAMIC_FILE_UPLOADED_BY_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        help_text=_('The owner/uploader of this file')
    )
    '''
    Specifies the uploader of this file. This foreign key defaults to AUTH_USER_MODEL
    but can be customized by changing DYNAMIC_FILE_UPLOADED_BY_MODEL.
    The reverse accessor is unused.

    NOTE: Changing those settings is only supported _before_ running the first migration
    '''

    @property
    def name(self):
        return self.file.name

    @property
    def read(self):
        return self.file.read

    @property
    def mimetype(self):
        return mimetypes.MimeTypes().guess_type(self.name)[0]

    def to_base64(self):
        return base64.b64encode(self.read())

    def to_base64_utf8(self):
        return self.to_base64().decode('utf-8')

    def to_base64_src(self):
        src = self.to_base64_utf8()
        return f'data:;base64,{src}'

    def __str__(self):
        '''
        String representation of this model.
        If a display name is set, this will be used as representation.
        If no display name is set, the filename is used.
        If no filename is set, the pk and a `_nofile` suffix is used.
        '''
        if len(self.display_name) > 0:
            return self.display_name
        elif len(self.name) > 0:
            return self.name
        else:
            return f'{self.pk}_nofile'

    class Meta:
        abstract = True
