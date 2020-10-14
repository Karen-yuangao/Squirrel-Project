"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path
from django.conf.urls import url
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.map),
    path('sightings/add/', views.add),
    path('sightings/', views.sightings),
    path('doadd/', views.doadd),
    path('doupdate/', views.doUpdate),
    re_path(r'^sightings/([\dA-Z]{2,3}-\b(AM|PM)\b-\d{4}-\d{2})/$',views.sightingsforupdate),
    path('sightings/stats/', views.stats),
]
