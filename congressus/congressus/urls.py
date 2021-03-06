"""congressus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^window/', include('windows.urls')),
    url(r'^access/', include('access.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^report/', include('dashboard.urls_report')),
    url(r'^invs/', include('invs.urls')),
    url(r'', include('tickets.urls')),
]

if 'theme' in settings.INSTALLED_APPS:
    urlpatterns += url(r'^custom/', include('theme.urls')),

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^debug/', include(debug_toolbar.urls)),
        url(r'^silk/', include('silk.urls', namespace='silk'))
    ]
