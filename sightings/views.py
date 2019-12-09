from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import generic
from .models import Sight
from django.template import loader
from django.shortcuts import render
from django.db import models
from django.template import loader
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from .forms import SightForm

def index(request):
    squi_list = Sight.objects.order_by('id')
    #output = '\n'.join([row.unique_squi_id for row in squi_list])
    template = loader.get_template('sightings/index.html')
    context = {
        'squi_list': squi_list,
    }
    return HttpResponse(template.render(context, request))


def s_id(request, user_id):
    data = Sight.objects.get(unique_squirrel_id = user_id) 
    if request.method == 'POST':
        form = SightForm(request.POST, instance = data)
        if form.is_valid():
            form.save(commit = True)
            return HttpResponseRedirect('/sightings/')
    else:
        form = SightForm(instance = data)
    return render(request, 'sightings/update.html', {'form':form})




def add(request):
    if request.method == 'POST':
        form = SightForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = SightForm()

    return render(request, 'sightings/add.html', {'form':form})




