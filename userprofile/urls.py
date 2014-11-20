"""
Urls conf for userprofiles
"""
from django.conf.urls import patterns, url
from userprofile import views as userviews

urlpatterns = patterns('',
  url(r'^profile/', userviews.update_profile),
)
