from django.core.management.base import BaseCommand
import pandas as pd
import csv
from sightings.models import Sight

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', nargs = '+', type = str)

    def handle(self, *args, **kwargs):
        with open(kwargs['path'][0]) as file:
            reader = csv.DictReader(file)
            data = list(reader)

        for item in data:
            s = Sight(
            x = item['x'],
            y = item['y'],
            unique_squi_id = item['unique_squirrel_id'],
            Shift = item['shift'],
            Date = item['date'],
            Age = item['age'],
            primary_fur_color = item['primary_fur_color'],
            Location = item['location'],
            specific_location = item['specific_location'],
            running = item['running'],
            Climbing = item['climbing'],
            Eating = item['eating'],
            Foraging = item['foraging'],
            other_activities = item['other_activities'],
            Kuks = item['kuks'],
            Quaas = item['quaas'],
            Moans = item['moans'],
            tail_flags = item['tail_flags'],
            tail_twitches = item['tail_twitches'],
            approaches = item['approaches'],
            indifferent = item['indifferent'],
            runs_from = item['runs_from'],
            )
            s.save()
        
         
