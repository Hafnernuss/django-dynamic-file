from rest_framework import serializers

from dynamic_file.models import DynamicFile


class _DynamicFileFieldMixin():
    _Model = DynamicFile()
    _view_name = None

    def get_attribute(self, instance):
        value = super().get_attribute(instance)
        return value if value else '__invalid__'

    def to_representation(self, dynamic_file):
        if dynamic_file == '__invalid__':
            method_name = f'get_{self.field_name}_fallback_url'
            method = getattr(self.parent, method_name, None)
            return method(self.parent.instance) if method else None

        method_name = f'get_{self.field_name}_url'
        method = getattr(self.parent, method_name)
        rep = method(dynamic_file)

        request = self.context.get('request', None)
        return request.build_absolute_uri(rep) if request else rep

    def run_validation(self, data):
        value = self.to_internal_value(data)
        self.run_validators(value)
        return value

    def to_internal_value(self, data):
        instance = self.parent.instance

        if data is None:
            asset = getattr(instance, self.field_name, None) if instance else None
            if asset:
                asset.delete()
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

    def __init__(
        self,
        view_name=None,
        view_args={},
        *args,
        **kwargs
    ):
        kwargs['use_url'] = False
        self.view_name = view_name
        self.view_args = view_args
        super().__init__(*args, **kwargs)
