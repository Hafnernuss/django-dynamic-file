from django.conf import settings

FALLBACK_METHOD_DEFAULT = 'DEFAULT'
FALLBACK_METHOD_NULL = 'NULL'

if not hasattr(settings, 'DYNAMIC_FILE_FALLBACK_METHOD'):
    setattr(settings, 'DYNAMIC_FILE_FALLBACK_METHOD', FALLBACK_METHOD_DEFAULT)

if not hasattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_MODEL'):
    setattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_MODEL', settings.AUTH_USER_MODEL)

if not hasattr(settings, 'DYNAMIC_FILE_STORAGE_LOCATION'):
    setattr(settings, 'DYNAMIC_FILE_STORAGE_LOCATION', 'files')

if not hasattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_MIGRATION_DEPENDENCY'):
    setattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_MIGRATION_DEPENDENCY', '__first__')

if not hasattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME'):
    setattr(settings, 'DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME', 'uploaded_files')
