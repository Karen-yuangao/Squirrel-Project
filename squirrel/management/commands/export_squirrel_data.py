from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

import csv

class Command(BaseCommand):
    help = 'Export data in CVS file'

    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **kwargs):
        fields = Squirrel._meta.fields
        with open(options['file'], 'w') as file:
            writer = csv.writer(file)
            for i in Squirrel.objects.all():
                row = [getattr(i, field.name) for field in fields]
                writer.writerow(row)
            file.close()
