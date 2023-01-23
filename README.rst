==========================
django-dynamic-file
==========================

.. image:: https://coveralls.io/repos/github/Hafnernuss/django-dynamic-file/badge.svg?branch=master
    :target: https://coveralls.io/github/Hafnernuss/django-dynamic-file?branch=master



A hopefully flexible approach to serving dynamic files with django.


Introduction
=============
Currently there are many other file handling libraries out there, most of them designed
to handle files efficiently, make use of various storage backends or provide a good admin integration.

This library aims at providing an easy interface for handling files in conjunction with django rest framework, providing
methods for applying generic permissions to serving, updating and deleting files.

This is done by wrapping `FileField` in their own model.

You may read more about the usage of this library `at the official documentation site`_.



.. _at the official documentation site: https://django-dynamic-file.readthedocs.io/en/latest/
