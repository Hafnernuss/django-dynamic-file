######################
django-dynamic-file
######################
A hopefully flexible approach to serving dynamic files with django.

==============
Introduction
==============
Currently there are many other file handling libraries out there, most of them designed
to handle files efficiently, make use of various storage backends or provide a good admin integration.

This library aims at providing an easy interface for handling files in conjunction with django rest framework, providing
methods for applying generic permissions to serving, updating and deleting files.

This is done by wrapping `FileField` in their own model.

The following documents provide a guide on how to install, configure and use this library.

.. toctree::
  :maxdepth: 2

  installation
  configuration


