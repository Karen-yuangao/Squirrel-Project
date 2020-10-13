from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

import csv

class Command(BaseCommand):
    help = 'Export data in CVS file'

    def add_arguments(self, parser):
        parser.add_argument('args', narg = '*', type=str)

    def handle(self, *args, **kwargs):
        with open(args[0], 'w') as file:
            writer = csv.writer(file)
            fields = Squirrel._meta.fields
            for i in Squirrel.objects.all():
                r = [getattr(i, field.name) for field in fields]
                writer.writerow(r)
            file.close()
