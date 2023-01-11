from dynamic_file.views import ServeDynamicFile

from rest_framework.permissions import IsAdminUser


class ServeTestFile(ServeDynamicFile):
    permission_classes = []
    lookup_field = 'pk'
    lookup_url_kwarg = 'key'
