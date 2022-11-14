from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

class DynamicFileBase(models.Model):
    description = models.TextField(
        blank=True,
        help_text=_('A description for this file')
    )

    uploaded_by = models.ForeignKey(settings.DYNAMIC_FILE_UPLOADED_BY,
        on_delete=models.SET_NULL,
        null=True,
        related_name=settings.DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME,
        help_text=_('The owner/uploader of this file')
    )
