from django.core.files.storage import FileSystemStorage
from django.conf import settings

class DynamicFileSystemStorage(FileSystemStorage):
    def __init__(self, location=settings.DYNAMIC_FILE_STORAGE_LOCATION):
        super().__init__(location=location, base_url='')
