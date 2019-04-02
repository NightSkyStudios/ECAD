"""ecad_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from main import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project_post/', views.project, name='project_post'),
    path('equipment/', views.equipment, name='equipment'),
    path('events/', views.events, name='events'),
    path('event/<id>', views.event, name='event'),
    path('docs/', views.docs, name='docs'),
    path('normbase/', views.normbase, name='normbase'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<id>', views.blogpost, name='blogpost'),
    re_path(r'^$', views.index, name='index'),
    path('map_project/<ar>', views.map_project, name='map_project'),
    path(r'tinymce/', include('tinymce.urls')),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
