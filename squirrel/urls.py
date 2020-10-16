from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name = 'squirrel'
urlpatterns =[
              path('map/', views.map),
              path('sightings/add/', views.add),
              path('sightings/', views.sightings),
              path('sightings/stats/', views.stats),
              path('sightings/<str:unique_squirrel_id>/',views.update),
             ]
