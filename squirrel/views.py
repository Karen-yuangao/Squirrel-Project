from django.shortcuts import render, redirect
from django.conf import settings
from .models import SquirrelCens
from django.forms.models import model_to_dict
from django.core import serializers
import random
from json import dumps

def map(request):
    positions = SquirrelCens.objects.all()[0:100]
    #print(positions[:])
    mapdata = dumps(serializers.serialize("json",list(positions), fields=('latitude', 'longitude')))
    #print(mapdata)
    context = {'data': mapdata}
    return render(request,'map.html',context)
    
def add(request):
    return render(request,'add.html')

def sightings(request):
    context ={} 
    context["squirrel_profile"] = SquirrelCens.objects.all() 
    return render(request,'sightings.html',context)
