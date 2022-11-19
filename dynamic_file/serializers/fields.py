from django.conf import settings
from django.urls import reverse
from rest_framework import serializers

from dynamic_file.models import DynamicFile


class _DynamicFileFieldMixin():
    _Model = DynamicFile()
    _view_name = None
    # def __init__(self, view_name=None, related_field_name=None, fallback_strategy=settings.DYNAMIC_FILE_FALLBACK_METHOD, *args, **kwargs):
    #     kwargs['use_url'] = False
    #     self.view_name = view_name
    #     self.related_field_name = related_field_name
    #     self.fallback_strategy = fallback_strategy
    #     super().__init__(*args, **kwargs)

    def get_attribute(self, instance):
        value = super().get_attribute(instance)
        if value is None:
            if self.fallback_strategy == 'IGNORE':
                nullImg = self._Model()
                setattr(nullImg, '__invalid__', True)
                path = ''
                if self.view_name:
                    path = reverse(self.view_name, kwargs={'pk': instance.id})
                else:
                    path = self.parent.get_fallback_url(instance)
                setattr(nullImg, '__url__', path)
                return nullImg
            elif self.fallback_strategy is None:
                pass
        return value

    def to_representation(self, instance):
        if hasattr(instance, '__invalid__'):
            rep = getattr(instance, '__url__')
        elif self.view_name and self.related_field_name:
            rep = reverse(self.view_name, kwargs={'pk': getattr(instance, self.related_field_name).id} )
        else:
            rep = self.parent.get_serve_url(instance)

        request = self.context.get('request', None)
        if request is not None:
            rep = request.build_absolute_uri(rep)
        return rep

    def to_internal_value(self, data):
        instance = self.parent.instance

        if data == '' and instance is not None and getattr(instance, self.field_name, None) is not None:
            asset = getattr(instance, self.field_name)
            asset.delete()
            return None
        elif data == '':
            return None
        elif instance is None or getattr(instance, self.field_name, None) is None:
            asset = self._Model.objects.create(file=data)
            return asset
        else:
            asset = getattr(instance, self.field_name)
            asset.file = data
            asset.save()
            return asset


class DynamicFileField(_DynamicFileFieldMixin, serializers.FileField):
    _Model = DynamicFile

    def __init__(self, view_name=None, related_field_name=None, fallback_strategy=settings.DYNAMIC_FILE_FALLBACK_METHOD, *args, **kwargs):
        kwargs['use_url'] = False
        self.view_name = view_name
        self.related_field_name = related_field_name
        self.fallback_strategy = fallback_strategy
        super().__init__(*args, **kwargs)