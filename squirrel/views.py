from django.shortcuts import render, redirect
from django.conf import settings
from .models import Squirrel
from django.forms.models import model_to_dict
from django.core import serializers
import random
from json import dumps
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound



def map(request):
    sightings = Squirrel.objects.all()[0:100]
    context = {'sightings': sightings}
    return render(request,'map.html',context)
    
def add(request):
    return render(request,'add.html')

def sightings(request):
    context ={} 
    context["squirrel_profile"] = Squirrel.objects.all() 
    return render(request,'sightings.html',context)

    
def doadd(request):
    if request.method == "POST":
        Squirrel.objects.create(
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
        context["squirrel_profile"] = Squirrel.objects.all() 
        return render(request,'sightings.html', context)

def sightingsforupdate(request,uniqueSquirrelID,param):
    print('param:',uniqueSquirrelID,param)
    profile = Squirrel.objects.get(unique_squirrel_id=uniqueSquirrelID)
    context = {'profile': model_to_dict(profile)}
    return render(request,'unique_sighting.html',context)

def stats(request):
    sightings_total = Sighting.objects.count()
    sightings_grey = Sighting.objects.filter(primary_fur_color='GREY').count()
    sightings_cinnamon = Sighting.objects.filter(primary_fur_color='CINNAMON').count()
    sightings_black = Sighting.objects.filter(primary_fur_color='BLACK').count()
    sightings_ground_plane = Sighting.objects.filter(location='GROUND_PLANE').count()
    sightings_above_ground = Sighting.objects.filter(location='ABOVE_GROUND').count()
    chasing_true = Sighting.objects.filter(chasing=True).count()
    chasing_false = Sighting.objects.filter(chasing=False).count()
    climbing_true = Sighting.objects.filter(climbing=True).count()
    climbing_false = Sighting.objects.filter(climbing=False).count() 
    eating_true = Sighting.objects.filter(eating=True).count()
    eating_false = Sighting.objects.filter(eating=False).count() 
    context = {
	    'sightings_total': sightings_total,
	    'sightings_grey': sightings_grey,
            'sightings_cinnamon': sightings_cinnamon,
	    'sightings_black': sightings_black,
            'sightings_ground_plane':sightings_ground_plane,
            'chasing_true': chasing_true,
            'chasing_false': chasing_false,
            'climbing_true': climbing_true,
            'climbing_false': climbing_false,
	    'eating_true':eating_true,
            'eating_false': eating_false,
            }   
    return render(request,'stats.html',context)



def doUpdate(request):
    if request.method == "POST":
        latitude = request.POST.get('latitude',None)
        longitude = request.POST.get('longitude',None)
        unique_squirrel_id = request.POST.get('unique_squirrel_id',None)
        shift = request.POST.get('shift',None)
        date = request.POST.get('date',None)
        age = request.POST.get('age',None)
        obj, created = Squirrel.objects.update_or_create(
            unique_squirrel_id = unique_squirrel_id,
            defaults = {'latitude':latitude,'longitude':longitude,'shift':shift,'date':date,'age':age},
        )
    print(obj,created)
    context = {}
    context["squirrel_profile"] = Squirrel.objects.all() 
    return render(request,'sightings.html', context)

