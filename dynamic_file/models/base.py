from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings


class DynamicFileBase(models.Model):
    '''
    Base model for handling dynamic files. Should not be used on it's own by
    consuming applications.
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
        related_name=settings.DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME,
        help_text=_('The owner/uploader of this file')
    )
    '''
    Specifies the uploader of this file. This foreign key defaults to AUTH_USER_MODEL
    but can be customized by changing DYNAMIC_FILE_UPLOADED_BY_MODEL.
    The reverse accessor defaults to 'uploaded_files' and can be customized by changing
    DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME.

    NOTE: Changing those settings is only supported _before_ running the first migration
    '''
