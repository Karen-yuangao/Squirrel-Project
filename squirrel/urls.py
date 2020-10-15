from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name = 'squirrel'
urlpatterns =[
              path('map/', views.map),
              path('sightings/add/', views.add),
              path('sightings/', views.sightings),
              path('doadd/', views.doadd),
              path('doupdate/', views.doUpdate),
              re_path(r'^sightings/([\dA-Z]{2,3}-\b(AM|PM)\b-\d{4}-\d{2})/$',views.sightingsforupdate),
              path('sightings/stats/', views.stats),
             ]
