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
    sightings = Squirrel.objects.all()[:100]
    context = {
            'sightings': sightings
    }
    return render(request,'map.html',context)

#add new sightings of squirrel locate on the sighting page and will direct to add page(in 'form')
def add(request):
     if request.method == "POST":
        form= SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
     else:
        form = SquirrelForm()
        context ={
              'form':form,
        }
    return render(request,'add.html',context)

#first page with Unique Squirrel ID, Date, and Link to unique squirrel sighting
def sightings(request):
    squirrel = Squirrel.objects.all()
    context = {
            'squirrels': squirrel,
    }
    return render(request, 'sightings.html',context)

#probablity need a form for this update part
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
	    'sightings_above_ground':sightings_above_ground ,
            'chasing_true': chasing_true,
            'chasing_false': chasing_false,
            'climbing_true': climbing_true,
            'climbing_false': climbing_false,
	    'eating_true':eating_true,
            'eating_false': eating_false,
            }   
    return render(request,'stats.html',context)
