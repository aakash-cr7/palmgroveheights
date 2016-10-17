"""palmgrove URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from account import views as account_views
from . import views as palmgrove_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', account_views.index),
    url(r'^register/$', account_views.signup, name='register'),
    url(r'^home/$', account_views.home, name='home'),
    url(r'^logout/$', account_views.logout, name='logout'),
    url(r'^discussions/$', palmgrove_views.discussions, name='discussions'),
    url(r'^notices/$', palmgrove_views.notices, name='notices'),
]
