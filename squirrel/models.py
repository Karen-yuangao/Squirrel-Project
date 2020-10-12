from django.db import models

from django.utils.translation import gettext as _


class Squirrel(models.Model):
     X = models.DecimalField(
         max_length=50,
         help_text=_('Longitude Coordinate for Squirrel sighting point'),
         blank = True,
         max_digits=20,
         decimal_places = 15,
    )

     Y = models.DecimalField(
         max_length=50,
         help_text=_('Latitude Coordinate for Squirrel sighting point'),
         blank = True,
         max_digits=20,
         decimal_places = 15,
    )

     Unique_Squirrel_ID= models.CharField(
         max_length=100,
         help_text=_('Identification tag for each squirrel sightings'),
         primary_key= True,
    )

     AM='AM'
     PM='PM'
     SHIFT_CHOICES =(
            (AM,'AM'),
            (PM,'PM'),
    )

     Shift  = models.CharField(
         max_length=100,
         choices = SHIFT_CHOICES,
         help_text=_('Squirrel sighting session occured in morning or afternoon'),
         blank = True,
    )

     Date = models.IntegerField(
         help_text=_('Session of sighting day and month'),
    )

     ADULT='Adult'
     JUVENILE = 'Juvenile'
     AGE_CHOICES = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
    )
            
     Age = models.CharField(
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

     Primary_Fur_Color = models.CharField(
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

     Location = models.CharField(
            max_length=50,
            choices = LOCATION_CHOICES,
            blank=True,
            help_text=_('Where the squirrel was when first sighted'),
    )

     Specific_Location = models.CharField(
            max_length=200,
            blank=True,
            help_text=_('Sighters occasional comment on the squirrel location'),
    )

     Running = models.BooleanField(
            help_text=_('Squirrel was seen running'),
            default = False,
    )

     Chasing = models.BooleanField(
            help_text=_('Squirrel was seen chasing'),
            default = False,
    )

     Climbing = models.BooleanField(
            help_text=_('Squirrel was seen climbing'),
            default= False,
    )

     Eating = models.BooleanField(
            help_text=_('Squirrel was seen eating'),
            default= False,
    )

     Foraging = models.BooleanField(
            help_text=_('Squirrel was seen foraging for food'),
            default = False,
    )

     Other_activities = models.CharField(
            max_length=200,
            blank=True,
            help_text=_('no description available '),
     )

     Kuks = models.BooleanField(
            help_text=_('Squirrel was heard kukking, a chirpy vocal communication'),
            default = False,
     )

     Quaas = models.BooleanField(
            help_text=_('Squirrel was heard quaaing, an elongated vocal communication'),
            default= False,
     )


     Moans = models.BooleanField(
            help_text=_('Squirrel was heard moaning, a high-pitched vocal communication'),
            default = False,
    )

     Tail_flags = models.BooleanField(
            help_text=_('Squirrel was seen flagging its tail'),
            default = False,
    )

     Tail_twitches = models.BooleanField(
            help_text=_('Squirrel was seen twitching its tail'),
            default= False,
    )

     Approaches = models.BooleanField(
            help_text=_('Squirrel was seen approaching human for food'),
            default= False,
    )

     Indifferent = models.BooleanField(
            help_text=_('Squirrel was indifferent to human presence'),
            default = False,
    )

     Runs_From = models.BooleanField(
            help_text=_('Squirrel was seen running from humans'),
            default= False,
    )

     def __str__(self):
         return self.Unique_Squirrel_ID


