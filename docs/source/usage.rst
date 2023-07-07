.. _usage:

######################
Usage
######################

This document will outline the installation process of this library.
This library uses models to store files. This means, three components are needed for serving/handling files:

#. Defining dynamic files in models
#. Adapting serializers
#. Defining views for file CRUD operations


***************************************************
Defining dynamic files in models
***************************************************

As an example, a model ``Company`` should have a ``dynamic file``, a ``ForeignKey`` (or ``OneToOneField``) has to be defined. As an example.

.. code-block:: python3

  from dynamic_file.models import DynamicFile
  from django.db import models

  class Company(models.Model):

    name = models.TextField()

    image = models.OneToOneField(
        DynamicFile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='company_image'
    )


***************************************************
Adapting serializers
***************************************************

To make use of the added file, the serializer has to be adapted. For this, a serializer field is provided
by the library. In essence, this field needs to be told which view is used for serving the file.

There are several ways of doing this, depending on the use case.
For the following examples, the following view definition is assumed:

.. code-block:: python3

  from dynamic_file.views import ServeDynamicFile

  urlpatterns = [
      path('serve/<int:pk>', ServeDynamicFile.as_view(), name='serve_default'),
  ]


Usage with method
****************************************************

.. code-block:: python3

  from dynamic_file.serializers import DynamicFileField
  from .models import Company

  class CompanySerializer(serializers.ModelSerializer):
      file = DynamicFileField(allow_null=True)

      def get_file_url(self, dynamic_file):
          return reverse('serve_default', kwargs={'pk': dynamic_file.id})

      class Meta:
          model = Company
          fields = ['file']


This method is similar to a standard ``SerializerMethodField`` and works in a similar fashion.
For each ``DynamicFileField``, a method needs to be defined, which follows the structure ``get_{field_name}_url(self, dynamic_file)``.
This method needs to return an url pointing to the serving url (For now, let's assume the view ``serve_default`` is defined somewhere).

**Pro**:

* Highly flexible: depending on the context, different serving urls can be used, and an arbitrary number of arguments can be passed

**Con**:

* Some developers might find this quite verbose, and for simple use cases, it maybe is.

Usage with arguments
****************************************************
A more concise way to specify the view would be using arguments for the ``DynamicFileField``:

.. code-block:: python3

  from dynamic_file.serializers import DynamicFileField
  from .models import Company

  class CompanySerializer(serializers.ModelSerializer):
      file = DynamicFileField(allow_null=True, view_name='serve_default', view_args={'pk': 'pk'})

      class Meta:
          model = Company
          fields = ['file']

Special attention has to be given to the passing of ``view_args``. The key is (as usual) the name of the view argument,
and the value is the *name* of the field on the ``DynamicFile``. The example above produces the **same** target url
as the example with the method.

**Pro**:

* More concise syntax

**Con**:

* Not as flexible, but sufficient for most use-cases.


Handling of null values
****************************************************
Sometimes, foreign keys to a ``DynamicFile`` are nullable. This is of course a perfectly acceptable use-case.
As a default (fallback), the serializer field will return ``null``/``None`` in this case. However, this behaviour can be adapted by specifying
a serializer method following the syntax ``get_{field_name}_fallback_url(self, instance)``:

.. code-block:: python3

    def get_file_fallback_url(self, instance):
        return reverse('some_default_view', kwargs={'pk': instance.id})

.. note::
   ``instance`` in this case refers to the model that has the ``DynamicFile`` attached, in this example an instance of ``Model``

***************************************************
Defining views
***************************************************
As stated earlier, defining custom views  is optional.
The provided default view is suitable for serving files identified by their primary key.
There is a provided default view which handles file serving via a passed ``pk``, with the default
``drf`` permssions applied. However, it is necessary to include this view in an ``urls.py`` file:


.. code-block:: python3

    from dynamic_file.views import ServeDynamicFile

    urlpatterns = [
      path('serve/<int:pk>', ServeDynamicFile.as_view(), name='serve_default'),
    ]


Now, this view name (``serve_default``) can be used in serializers, as described above.


***************************************************
Admin integration
***************************************************
``DynamicFile`` has a pretty basic but useful admin integration.
It supports a preview rendering in case the file is an image.
In case it's not an image, no preview will be shown.


.. code-block:: python3

    from .models import Company
    from django.contrib import admin

    from dynamic_file.admin import preview as image_preview

    @admin.register(Company)
    class CompanyAdmin(admin.ModelAdmin):
        fields = ['image', 'preview']
        readonly_fields = ['preview']

        def preview(self, instance):
            return image_preview(instance.image)


Files can also be downloaded from within the admin with a provided view.
Simply add the following to your ``urls.py`` and make sure that you place it
**before** the actual import of the admin pages:

.. code-block:: python3

  from dynamic_file.views import ServeDynamicFileAdmin

  urlpatterns = [

      #... your other includes

      path('admin/download/<str:name>', ServeDynamicFileAdmin.as_view()),
      path('admin/', admin.site.urls),
  ]



This enables downloadable files for every user that has access to the admin page.
