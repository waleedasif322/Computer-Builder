"""
The url conf for builds app
"""
import builds.views
from django.conf.urls import url, patterns, include
from ajax_select import urls as ajax_select_urls




urlpatterns = patterns('',

    url(r'^new_build/$', builds.views.new_build),
    url(r'^build_confirmation/$', builds.views.create_build),
    url(r'^edit_build/(?P<build_name>\w+)/$', builds.views.edit_build),
    url(r'^edit/$', builds.views.edit_list),
    url(r'^show/(?P<build_name>\w+)/$', builds.views.show_build),
    url(r'^mybuilds/$', builds.views.show_mybuilds),
    url(r'^home/$', builds.views.home_page),
    url(r'^public_builds/$', builds.views.show_pubbuilds),
    url(r'^autocomplete/', include(ajax_select_urls)),
    url(r'^delete/(?P<build_name>\w+)/$', builds.views.delete),
    url(r'^search/', builds.views.search),
)
