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
import pandas as pd
from .models import Sight

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from .forms import SightForm
from django.http import HttpResponseRedirect
from pylab import *
import PIL, PIL.Image
from io import BytesIO
from matplotlib import pylab



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

def stats(request):
    squirrels=pd.read_csv('file.csv')

    x_age = squirrels['age'].value_counts().index
    y_age = squirrels['age'].value_counts()

    x_fur = squirrels['primary_fur_color'].value_counts().index
    y_fur = squirrels['primary_fur_color'].value_counts()

    x_loc = squirrels['location'].value_counts().index
    y_loc = squirrels['location'].value_counts()

    x_shift = squirrels['shift'].value_counts().index
    y_shift = squirrels['shift'].value_counts()

    x_run = squirrels['running'].value_counts().index
    y_run = squirrels['running'].value_counts()

    x_cha = squirrels['chasing'].value_counts().index
    y_cha = squirrels['chasing'].value_counts()

    x_cli = squirrels['climbing'].value_counts().index
    y_cli = squirrels['climbing'].value_counts()

    x_eat = squirrels['eating'].value_counts().index
    y_eat = squirrels['eating'].value_counts()

    fig, axs = plt.subplots(2, 4, figsize=(30,15))
    fig.suptitle('SQUIRREL STATS', fontsize=50)

    axs[0,0].bar(x_age, height=y_age, color=(0, 0.7, 0))
    axs[0,0].set_title('Squirrels by Age', fontsize=30)
    axs[0,0].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0,0].tick_params(axis='both', which='major', labelsize=20)

    axs[0,1].bar(x_fur, height=y_fur, color=(1, 0.7, 0))
    axs[0,1].set_title('Squirrels by Primary Fur Color', fontsize=30)
    axs[0,1].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0,1].tick_params(axis='both', which='major', labelsize=20)

    axs[0,2].bar(x_loc, height=y_loc, color=(0, 0, 1))
    axs[0,2].set_title('Squirrels by Location', fontsize=30)
    axs[0,2].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0,2].tick_params(axis='both', which='major', labelsize=20)

    axs[0,3].bar(x_shift, height=y_shift, color=(0, 1, 0))
    axs[0,3].set_title('Squirrels by AM/PM', fontsize=30)
    axs[0,3].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0,3].tick_params(axis='both', which='major', labelsize=20)


    axs[1,0].bar(x_run, height=y_run, color=(0, 0.7, 0))
    axs[1,0].set_xlabel('Running Squirrels', fontsize=25)
    axs[1,0].set_ylabel('Frequency of sightings', fontsize=25)
    axs[1,0].tick_params(axis='both', which='major', labelsize=20)

    axs[1,1].bar(x_cha, height=y_cha, color=(1, 0.7, 0))
    axs[1,1].set_xlabel('Chasingi squirrels', fontsize=25)
    axs[1,1].set_ylabel('Frequency of sightings', fontsize=25)
    axs[1,1].tick_params(axis='both', which='major', labelsize=20)

    axs[1,2].bar(x_cli, height=y_cli, color=(0, 0, 1))
    axs[1,2].set_xlabel('Climbing squirrels', fontsize=25)
    axs[1,2].set_ylabel('Frequency of sightings', fontsize=25)
    axs[1,2].tick_params(axis='both', which='major', labelsize=20)

    axs[1,3].bar(x_eat, height=y_eat, color=(0, 1, 0))
    axs[1,3].set_xlabel('Eating squirrels', fontsize=25)
    axs[1,3].set_ylabel('Frequency of sightings', fontsize=25)
    axs[1,3].tick_params(axis='both', which='major', labelsize=20)

    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    return HttpResponse(buffer.getvalue(), content_type="image/png")
