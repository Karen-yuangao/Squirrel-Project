from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from .models import Squirrel
from .forms import SquirrelForm
from django.db.models import Count


def update(request,unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method =='POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm(instance=squirrel)

    context ={
            'form':form,
             }
    return render(request, 'squirrel/update.html', context)

def map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
            'sightings': sightings
    }
    return render(request,'squirrel/map.html',context)

#add new sightings of squirrel locate on the sighting page and will direct to add page(in 'form')
def add(request):
     if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            ID = form['unique_squirrel_id'].value()
            form.save()
            return redirect(f'/sightings')
     else:
         form = SquirrelForm()
         context ={
                 'form':form,
         }
     return render(request,'squirrel/add.html',context)


#first page with Unique Squirrel ID, Date, and Link to unique squirrel sighting
def sightings(request):
    squirrels= Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'squirrel/sightings.html',context)


def stats(request):
    sightings_total = Squirrel.objects.count()
    sightings_grey = Squirrel.objects.filter(primary_fur_color='Gray').count()
    sightings_cinnamon = Squirrel.objects.filter(primary_fur_color='Cinnamon').count()
    sightings_black = Squirrel.objects.filter(primary_fur_color='Black').count()
    sightings_ground_plane = Squirrel.objects.filter(location='Ground Plane').count()
    sightings_above_ground = Squirrel.objects.filter(location='Above Ground').count()
    chasing_true = Squirrel.objects.filter(chasing=True).count()
    chasing_false = Squirrel.objects.filter(chasing=False).count()
    climbing_true = Squirrel.objects.filter(climbing=True).count()
    climbing_false = Squirrel.objects.filter(climbing=False).count() 
    eating_true = Squirrel.objects.filter(eating=True).count()
    eating_false = Squirrel.objects.filter(eating=False).count() 
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
    return render(request,'squirrel/stats.html',context)


