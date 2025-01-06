from django.conf import settings
from django.http.response import FileResponse
from django.http.response import HttpResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound

from dynamic_file.models import DynamicFile

from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

import mimetypes
import os


class _DynamicContentMixin():
    _Model = DynamicFile
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def get_object(self):
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        instance = self._Model.objects.filter(**filter_kwargs).first()
        self.check_object_permissions(self.request, instance)
        return instance


class ServeDynamicFile(_DynamicContentMixin, APIView):
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        filename = None
        if instance:
            filename = instance.file.name
        else:
            raise NotFound()

        content_type, encoding = mimetypes.guess_type(filename)
        path = os.path.join(settings.DYNAMIC_FILE_SERVE_LOCATION, filename)

        try:
            if settings.DEBUG:
                fp = open(path, 'rb')
                response = FileResponse(fp)
                response.filename = filename

            else:  # for now, nginx will suffice
                response = HttpResponse(content_type=content_type)
                response['Content-Disposition'] = 'inline; filename={0}'.format(filename)
                response['Content-Encoding'] = encoding

                location = os.path.normpath(path)
                response['X-Accel-Redirect'] = f'/{location}'

            return response
        except Exception as e:
            print(e)
            return HttpResponse('File not found', status=status.HTTP_404_NOT_FOUND)


class ServeDynamicFileAdmin(ServeDynamicFile):
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'file'
    lookup_url_kwarg = 'name'
