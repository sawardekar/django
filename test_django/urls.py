"""test_django URL Configuration

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
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done,password_reset_confirm
urlpatterns = [
    url(r'^$', include('login.urls')),
    # url(r'^login/$',login,{'template_name':'login/login_form.html'}),
	url(r'^login/', include('login.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^music/', include('music.urls')),
    url(r'^reset-password/$', password_reset, name='password_reset'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>,+)/$', password_reset_confirm, name='password_reset_confirm')
]
