.. _changelog:

######################
Changelog
######################
This document provides an overview about breaking changes and new features.


***************************************************
0.6.0
***************************************************

Changes
****************************************************
The setting ``DYNAMIC_FILE_SERVE_LOCATION`` has been added.
This is useful for containerized production environments
where the serve location not necessarily corresponds to
the physical location.

***************************************************
0.5.0
***************************************************

Changes
****************************************************
The setting ``DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME`` has been removed.
If you want to know the uploaded files from your ``uploader entity``, use the following:

.. code-block:: python3

  DynamicFile.objects.filter(uploaded_by=your_entity_id)

Features
****************************************************

* If the file is an image, a preview will be shown in the admin (relies on ``mimetypes``)
* Added a field ``display_name`` to provide a human-readable name for dynamic files
* Added some ``base64`` utilities for commonly used tasks

***************************************************
0.4.0
***************************************************
First useable version
