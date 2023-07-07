from django.urls import path
from django.contrib import admin

from dynamic_file.views import ServeDynamicFile
from dynamic_file.views import ServeDynamicFileAdmin

from test_app.views import ServeTestFile

urlpatterns = [

    path('serve/<int:pk>', ServeDynamicFile.as_view(), name='serve_default'),
    path('customServe/<int:key>', ServeTestFile.as_view(), name='serve_custom'),

    path("admin/download/<str:name>", ServeDynamicFileAdmin.as_view()),
    path("admin/", admin.site.urls),
]
