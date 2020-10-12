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

        with open(path, 'rt') as f:
            reader = csv.DictReader(f)
            for r in reader:
                squirrel = Squirrel(
                    X = r['X'],
                    Y = r['Y'],
                    Unique_squirrel_id = r['Unique Squirrel ID'],
                    Shift = r['Shift'],
                    Date=datetime.date(
                        int(r['Date'][-4:]), int(r['Date'][:2]), int(r['Date'][2:4])),
                    Age = r['Age'],
                    Primary_Fur_Color = r['Primary Fur Color'],
                    Location = r['Location'],
                    Specific_location=r['Specific Location'],
                    Running = strtobool(r['Running']),
                    Chasing = strtobool(r['Chasing']),
                    Climbing = strtobool(r['Climbing']),
                    Eating = strtobool(r['Eating']),
                    Foraging = strtobool(r['Foraging']),
                    Other_activities = r['Other Activities'],
                    Kuks = strtobool(r['Kuks']),
                    Quaas = strtobool(r['Quaas']),
                    Moans = strtobool(r['Moans']),
                    Tail_flags = strtobool(r['Tail flags']),
                    Tail_twitches = strtobool(r['Tail twitches']),
                    Approaches = strtobool(r['Approaches']),
                    Indifferent = strtobool(r['Indifferent']),
                    Runs_From = strtobool(r['Runs from']),
                )
                s.save()
