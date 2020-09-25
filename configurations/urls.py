from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin', include('rest_framework.urls', namespace='rest')),
    path('api/field/', include(('app_dir.field.api.urls', 'field_api'), \
        namespace='field_api')),
    path('api/register/', include(('app_dir.register.api.urls', 'register_api'), \
        namespace='register_api'))
]

