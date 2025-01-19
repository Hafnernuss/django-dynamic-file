.. _configuration:

######################
Configuration
######################

The following configuration options are available:

DYNAMIC_FILE_STORAGE_LOCATION
****************************************************
.. code-block:: python3

  DYNAMIC_FILE_STORAGE_LOCATION = 'files'

Defines the location for uploaded files.

DYNAMIC_FILE_SERVE_LOCATION
****************************************************
.. code-block:: python3

  DYNAMIC_FILE_SERVE_LOCATION = DYNAMIC_FILE_STORAGE_LOCATION

Defines the base location from which files are served.
Defaults to DYNAMIC_FILE_STORAGE_LOCATION.
This parameter is most useful in production environments
where your application is containerized and files are served
via a reverse proxy. In such setups, the path for serving does not
necesarily correspond with the real physical location

Next Steps
****************************************************
An in-depth usage guide is available :ref:`here <usage>`.
