from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

from distutils.util import strtobool

import datetime

import csv

class Command(BaseCommand):
    help = 'Import squirrel data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        Squirrel.objects.all().delete()

        with open(path, 'rt') as f:
            reader = csv.DictReader(f)
            Data = list(reader)
            for r in Data:
               squirrel=Squirrel.objects.create(
                    longitude = r['X'],
                    latitude = r['Y'],
                    unique_squirrel_id = r['Unique Squirrel ID'],
                    shift = r['Shift'],
                    date=datetime.date(
                        int(r['Date'][-4:]), int(r['Date'][:2]), int(r['Date'][2:4])),
                    age = r['Age'],
                    primary_fur_color = r['Primary Fur Color'],
                    location = r['Location'],
                    specific_location=r['Specific Location'],
                    running = strtobool(r['Running']),
                    chasing = strtobool(r['Chasing']),
                    climbing = strtobool(r['Climbing']),
                    eating = strtobool(r['Eating']),
                    foraging = strtobool(r['Foraging']),
                    other_activities = r['Other Activities'],
                    kuks = strtobool(r['Kuks']),
                    quaas = strtobool(r['Quaas']),
                    moans = strtobool(r['Moans']),
                    tail_flags = strtobool(r['Tail flags']),
                    tail_twitches = strtobool(r['Tail twitches']),
                    approaches = strtobool(r['Approaches']),
                    indifferent = strtobool(r['Indifferent']),
                    runs_from = strtobool(r['Runs from']),
                )
            squirrel.save()

