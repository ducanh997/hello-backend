"""hello_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import routers

from hello_backend.views.auth import GoogleLoginView
from hello_backend.views.board import BoardViewSet
from hello_backend.views.workspace import WorkspaceViewSet


class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_operation(self, *args, **kwargs):
        operation = super().get_operation(*args, **kwargs)
        accept_language_header = openapi.Parameter(
            name='Accept-Language',
            description="Accept-Language",
            required=False,
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            default='vi'
        )
        operation.parameters.append(accept_language_header)
        return operation


schema_view = get_schema_view(
    openapi.Info(
        title="Hello Backend",
        default_version='v1',
        contact=openapi.Contact(email="ducanhk60uet@gmail.com"),
    ),
    public=True,
    generator_class=CustomSchemaGenerator,
    authentication_classes=()
)

router = routers.DefaultRouter()
router.register(r'workspaces', WorkspaceViewSet)
router.register('boards', BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/google/login/', GoogleLoginView.as_view(), name='login-with-google'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
