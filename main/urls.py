"""itsankur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from .views import *
from django.conf.urls import url

app_name="main"

urlpatterns = [
    path("", homepage, name="homepage"),
    path('contact/', contact, name = 'contact'),
    path('blog/', blog, name = 'blog'),
    path('myprojects/', myprojects, name = 'myprojects'),
    url(r'^getdata/', contact),
    url(r'^$', contact),
]
