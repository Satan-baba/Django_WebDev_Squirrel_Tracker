from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import generic
from .models import Sight
from django.template import loader
from django.shortcuts import render
from django.db import models
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory

from .forms import SightForm

def index(request):
    squi_list = Sight.objects.order_by('id')
    #output = '\n'.join([row.unique_squi_id for row in squi_list])
    template = loader.get_template('sightings/index.html')
    context = {
        'squi_list': squi_list,
    }
    return HttpResponse(template.render(context, request))

def second(request, unique_squi_id):
    try:
        row = Sight.objects.get(unique_squi_id = unique_squi_id)
    except:
        raise Http404("Does not exists")

    return render(request, 'sightings/second.html', {'row':row})
# Create your views here

def add(request):
    if request.method == 'POST':
        form = SightForm(request.POST)
        if form.is_valid():
            x = form.x
            
            return HttpResponseRedirect('/sightings/')
    else:
            form = SightForm()
            

    return render(request, 'sightings/add2.html', {'form': form})

