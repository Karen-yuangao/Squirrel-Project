from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
     latitude = models.DecimalField(
         max_length=50,
         help_text=_('Longitude Coordinate for Squirrel sighting point'),
         blank = True,
         max_digits=20,
         decimal_places = 15,
    )

     longitude = models.DecimalField(
         max_length=50,
         help_text=_('Latitude Coordinate for Squirrel sighting point'),
         blank = True,
         max_digits=20,
         decimal_places = 15,
    )

     unique_squirrel_id= models.CharField(
         max_length=100,
         help_text=_('Identification tag for each squirrel sightings'),
         primary_key= True,
    )

     AM ='AM'
     PM ='PM'
     SHIFT_CHOICES =(
            (AM,'AM'),
            (PM,'PM'),
    )

     shift = models.CharField(
         max_length=100,
         choices = SHIFT_CHOICES,
         help_text=_('Squirrel sighting session occured in morning or afternoon'),
         blank = True,
    )

     date = models.DateField(
         help_text=_('Session of sighting day and month'),
    )

     ADULT='Adult'
     JUVENILE = 'Juvenile'
     AGE_CHOICES = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
    )
            
     age = models.CharField(
         max_length=50,
         choices = AGE_CHOICES,
         blank = True,
    )

     GREY= 'Grey'
     CINNAMON= 'Cinnamon'
     BLACK = 'Black'
     COLOR_CHOICES = (
            (GREY,'Grey'),
            (CINNAMON,'Cinnamon'),
            (BLACK,'Black'),
    )

     primary_fur_color = models.CharField(
            max_length=10,
            blank=True,
            choices= COLOR_CHOICES,
            help_text=_('fur color'),
    )

     GROUND_PLANE = 'Ground Plane'
     ABOVE_GROUND = 'Above Ground'
     LOCATION_CHOICES =(
            (GROUND_PLANE,'Ground Plane'),
            (ABOVE_GROUND,'Above Ground'),
    )

     location = models.CharField(
            max_length=50,
            choices = LOCATION_CHOICES,
            blank=True,
            help_text=_('Where the squirrel was when first sighted'),
    )

     specific_location = models.CharField(
            max_length=200,
            blank=True,
            help_text=_('Sighters occasional comment on the squirrel location'),
    )

     running = models.BooleanField(
            help_text=_('Squirrel was seen running'),
            default = False,
    )

     chasing = models.BooleanField(
            help_text=_('Squirrel was seen chasing'),
            default = False,
    )

     climbing = models.BooleanField(
            help_text=_('Squirrel was seen climbing'),
            default= False,
    )

     eating = models.BooleanField(
            help_text=_('Squirrel was seen eating'),
            default= False,
    )

     foraging = models.BooleanField(
            help_text=_('Squirrel was seen foraging for food'),
            default = False,
    )

     other_activities = models.CharField(
            max_length=200,
            blank=True,
            help_text=_('no description available '),
     )

     kuks = models.BooleanField(
            help_text=_('Squirrel was heard kukking, a chirpy vocal communication'),
            default = False,
     )

     quaas = models.BooleanField(
            help_text=_('Squirrel was heard quaaing, an elongated vocal communication'),
            default= False,
     )


     moans = models.BooleanField(
            help_text=_('Squirrel was heard moaning, a high-pitched vocal communication'),
            default = False,
    )

     tail_flags = models.BooleanField(
            help_text=_('Squirrel was seen flagging tail'),
            default = False,
    )

     tail_twitches = models.BooleanField(
            help_text=_('Squirrel was seen twitching tail'),
            default= False,
    )

     approaches = models.BooleanField(
            help_text=_('Squirrel was seen approaching human for food'),
            default= False,
    )

     indifferent = models.BooleanField(
            help_text=_('Squirrel was indifferent to human presence'),
            default = False,
    )

     runs_from = models.BooleanField(
            help_text=_('Squirrel was seen running from humans'),
            default= False,
    )

     def __str__(self):
         return self.Unique_Squirrel_ID


