"""
URL configuration for editeblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),

    # AllAuth URLs
    path('accounts/', include('allauth.urls')),

    # TinyMCE URLs
    path('tinymce/', include('tinymce.urls')),

    # JavaScript catalog for TinyMCE
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),

    # Blog app URLs
    path('', include('blog.urls')),
]
