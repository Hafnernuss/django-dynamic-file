from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

import swapper
class DynamicFileBase(models.Model):
    description = models.TextField(
        blank=True,
        help_text=_('A description for this file')
    )

    uploaded_by = models.ForeignKey(settings.DYNAMIC_FILE_UPLOADED_BY,
        on_delete=models.SET_NULL,
        null=True,
        help_text=_('The owner/uploader of this file')
    )

    class Meta:
        abstract = True