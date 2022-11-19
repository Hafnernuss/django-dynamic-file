from django.conf import settings
from django.http.response import FileResponse
from django.http.response import HttpResponse

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from dynamic_file.models import DynamicFile

import mimetypes
import os


class ServeDynamicContentMixin():
    _Model = DynamicFile
    permission_classes = []

    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def get_file_name(self, file, _):
        _, ext = os.path.splitext(file.name)
        if not ext:
            return file.name + mimetypes.guess_extension(file.content_type)
        else:  # pragma: no cover
            return file.name

    def get_parent(self):
        return None

    def get_object(self):
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        qs = self._Model.objects.filter(**filter_kwargs)
        if qs.count() == 0:
            return None
        return qs.first()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        filename = None
        if instance:
            filename = instance.file.name

        # fallback would go here.

        content_type, encoding = mimetypes.guess_type(filename)
        path = os.path.join(settings.DYNAMIC_FILE_STORAGE_LOCATION, filename)

        # TODO check if exists and add fallback

        if settings.DEBUG:
            img = open(path, 'rb')
            response = FileResponse(img)

        else:  # for now, nginx will suffice
            response = HttpResponse(content_type=content_type)
            response["Content-Disposition"] = "inline; filename={0}".format(filename)
            response["Content-Encoding"] = encoding

            location = os.path.normpath(path)
            response['X-Accel-Redirect'] = location

        return response
