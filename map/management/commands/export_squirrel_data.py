from django.core.management.base import BaseCommand
import pandas as pd
#from . import import_squirrel_data
import csv
from sightings.models import Sight
                                           
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', nargs = '+', type = str)
    def handle(self, *args, **kwargs):
        path = kwargs['path'][0]
        s = Sight.objects.all()
        df = pd.DataFrame(s.values())
        df.to_csv(path)

