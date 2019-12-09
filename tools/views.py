from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    return HttpResponse('<h1>Hi Mr. Joffrey Hosencratz</h1><h2><a href = "/map/">Click here to view the map</a></h2><h2><a href = "/sightings/">Click here to view stats, add and edit Sightings</a></h2><img src = "https://heavyeditorial.files.wordpress.com/2017/09/img_0956.jpg?quality=65&strip=all&strip=all", height = "400", width = "400">')
