from django.shortcuts import render
from django.http import HttpResponse
from sightings.models import Sight
from django.template import loader
def index(request):
    sightings = Sight.objects.all()
    template = loader.get_template('map/maps.html')
    context = {'sightings':sightings}
    return HttpResponse(template.render(context, request))
