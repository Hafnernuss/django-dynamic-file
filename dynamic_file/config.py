from django.conf import settings

FALLBACK_METHOD_DEFAULT = 'DEFAULT'
FALLBACK_METHOD_NULL = 'NULL'

if not hasattr(settings, 'DYNAMIC_FILE_FALLBACK_METHOD'):
    setattr(settings, 'DYNAMIC_FILE_FALLBACK_METHOD', FALLBACK_METHOD_DEFAULT)

if not hasattr(settings, 'DYNAMIC_FILE_UPLOADED_BY'):
    setattr(settings, 'DYNAMIC_FILE_UPLOADED_BY', settings.AUTH_USER_MODEL)
