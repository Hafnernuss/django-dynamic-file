from dynamic_file.views import ServeDynamicFile

class ServeTestFile(ServeDynamicFile):
    permission_classes = []
    lookup_field = 'pk'
    lookup_url_kwarg = 'key'
