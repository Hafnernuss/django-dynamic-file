from django.urls import path

from dynamic_file.views import ServeDynamicFile

urlpatterns = [

    path('serve/<int:pk>', ServeDynamicFile.as_view(), name='serve_default'),

]
