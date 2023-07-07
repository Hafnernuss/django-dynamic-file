######################
Installation & Setup
######################

This document will outline the installation process of this library.

**********************
Install from pypi
**********************
This library can be installed from pypi via the following command:

.. code-block:: bash

    pip install django-dynamic-file


**********************
Install from GitHub
**********************
This library can be directly installed form github via the following command:

.. code-block:: bash

    pip install git+https://github.com/Hafnernuss/django-dynamic-file@master


**********************
Add to installed apps
**********************
Simply add ``dynamic_file`` to your installed apps inside ``settings.py`` file:

.. code-block:: python3

  INSTALLED_APPS = [
    '...',
    'dynamic_file',
    '...',
  ]

**************************
First time configuration
**************************
``dynamic_file`` has to be set up with a minimal configuration which has to be defined before the first migration.
All those settings do have a default value, but depending on the use-case, adaptions can be necessary.
If one settings has to be changed, they have to be defined inside the ``settings.py`` file.


DYNAMIC_FILE_UPLOADED_BY_MODEL
****************************************************
.. code-block:: python3

  DYNAMIC_FILE_UPLOADED_BY_MODEL = AUTH_USER_MODEL

This setting defines the foreign key that determines which entity has uploaded the file. It defaults to the user model.


DYNAMIC_FILE_UPLOADED_BY_MODEL_MIGRATION_DEPENDENCY
****************************************************
.. code-block:: python3

  DYNAMIC_FILE_UPLOADED_BY_MODEL_MIGRATION_DEPENDENCY = '__first__'

In case the model specified by ``DYNAMIC_FILE_UPLOADED_BY_MODEL`` is not the initial migration, the actual migration
step can be defined here.

Next Steps
****************************************************
When all above parameters are checked and/or adapted, initial migrations should be performed:

.. code-block:: python3

  python manage.py migrate

| Further configuration parameters can be reviewed :ref:`here <configuration>`.
| An in-depth usage guide is available :ref:`here <usage>`.
