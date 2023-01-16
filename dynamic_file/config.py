from django.conf import settings

if not hasattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_MODEL'):
    setattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_MODEL', settings.AUTH_USER_MODEL)

if not hasattr(settings, 'DYNAMIC_FILE_STORAGE_LOCATION'):
    setattr(settings, 'DYNAMIC_FILE_STORAGE_LOCATION', 'files')

if not hasattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_MIGRATION_DEPENDENCY'):
    setattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_MIGRATION_DEPENDENCY', '__first__')

if not hasattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME'):
    setattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME', 'uploaded_files')
