from django.urls import path

from dynamic_file.views import ServeDynamicFile

from test_app.views import ServeTestFile

urlpatterns = [

    path('serve/<int:pk>', ServeDynamicFile.as_view(), name='serve_default'),
    path('customServe/<int:key>', ServeTestFile.as_view(), name='serve_custom'),

]
