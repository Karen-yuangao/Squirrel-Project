from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

import csv

class Command(BaseCommand):
    help = 'Export data in CVS file'

    def add_arguments(self, parser):
        parser.add_argument('exported_csv_file')

    def handle(self, *args, **kwargs):
        with open(kwargs['exported_csv_file'], 'w') as f:
            writer = csv.writer(f)
            fields = Squirrel._meta.fields
            for i in Squirrel.objects.all():
                r = [getattr(i, field.name) for field in fields]
                writer.writerow(r)
            f.close()
