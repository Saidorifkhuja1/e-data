# """
# URL configuration for core project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
#
# """
# URL configuration for core project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from aiohttp.web_routedef import static
# from django.contrib import admin
# from django.urls import path, include, re_path
# from django.views.static import serve
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from drf_yasg.generators import OpenAPISchemaGenerator
#
# from core import settings
#
#
# class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
#     def get_schema(self, request=None, public=False):
#         schema = super().get_schema(request, public)
#         schema.schemes = ["http", "https"]
#         return schema
#
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="E-Data  API",
#       default_version='v1',
#    ),
#    public=True,
#    generator_class=BothHttpAndHttpsSchemaGenerator,
#    permission_classes=(permissions.AllowAny,),
# )
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/user/', include('user.urls')),
#     path('api/file/', include('file.urls')),
#     # path('api/books/', include('books.urls')),
#     # path('api/news/', include('news.urls')),
#     path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#
#     re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#     re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
# ]




from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from core import settings

class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema

schema_view = get_schema_view(
   openapi.Info(
      title="E-Data API",
      default_version='v1',
   ),
   public=True,
   generator_class=BothHttpAndHttpsSchemaGenerator,
   permission_classes=(permissions.AllowAny,),
)

# Root route
def home_view(request):
    return JsonResponse({"message": "Welcome to the E-Data API"})

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/file/', include('file.urls')),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
