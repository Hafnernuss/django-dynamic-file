######################
Installation & Setup
######################

This document will outline the installation process of this library.

**********************
Install from pypy
**********************
TBD, once this library has reached a certain stable state.

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
******************************
.. code-block:: python3

  DYNAMIC_FILE_UPLOADED_BY_MODEL = AUTH_USER_MODEL

This setting defines the foreign key that determines which entity has uploaded the file. It defaults to the user model.


DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME
******************************
.. code-block:: python3

  DYNAMIC_FILE_UPLOADED_BY_RELATED_NAME = 'uploaded_files'

Defines the related name for all uploaded files that is added to the model specified by ``DYNAMIC_FILE_UPLOADED_BY_MODEL``.

Before running any migrations, it is **highly** recommended to read the :ref:`configuration guide <configuration>`.


DYNAMIC_FILE_UPLOADED_BY_MODEL_MIGRATION_DEPENDENCY
******************************
.. code-block:: python3

  DYNAMIC_FILE_UPLOADED_BY_MODEL_MIGRATION_DEPENDENCY = '__first__'

In case the model specified by ``DYNAMIC_FILE_UPLOADED_BY_MODEL`` is not the initial migration, the actual migration
step can be defined here.

Before running any migrations, it is **highly** recommended to read the :ref:`configuration guide <configuration>`.
