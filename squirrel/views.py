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

    
def doadd(request):
    if request.method == "POST":
        SquirrelCens.objects.create(
            latitude = request.POST.get('latitude',None),
            longitude = request.POST.get('longitude',None),
            unique_squirrel_id = request.POST.get('unique_squirrel_id',None),
            shift = request.POST.get('shift',None),
            date = request.POST.get('date',None),
            age = request.POST.get('age',None),
            primary_fur_color = request.POST.get('primary_fur_color',None),
            location = request.POST.get('location',None),
            specific_location = request.POST.get('specific_location',None),
            running = request.POST.get('running',None),
            chasing = request.POST.get('chasing',None),
            climbing = request.POST.get('climbing',None),
            eating = request.POST.get('eating',None),
            foraging = request.POST.get('foraging',None),
            other_activities = request.POST.get('other_activities',None),
            kuks = request.POST.get('kuks',None),
            quaas = request.POST.get('quaas',None),
            moans = request.POST.get('moans',None),
            tail_flags = request.POST.get('tail_flags',None),
            tail_twitches = request.POST.get('tail_twitches',None),
            approaches = request.POST.get('approaches',None),
            indifferent = request.POST.get('indifferent',None),
            runs_from = request.POST.get('runs_from',None)
		)
        context ={}
        context["squirrel_profile"] = SquirrelCens.objects.all() 
        return render(request,'sightings.html', context)
