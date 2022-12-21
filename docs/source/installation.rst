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

Before running any migrations, it is **highly** recommended to read the :ref:`configuration guide <configuration>`.