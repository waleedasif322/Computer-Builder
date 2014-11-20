"""
Urls.py module for our main app
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
import computerbuilder.views as views
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.cover_page),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^builds/', include('builds.urls')),
    #url(r'^accounts/', include('registration_app.urls')), 
    url(r'^new_build', view='builds.views.new_build', name='new_build'),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^about/', views.about_page),
    url(r'^contact/', views.contact_page),
)
