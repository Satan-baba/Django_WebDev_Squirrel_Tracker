from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import requests
import folium
from geojson import Feature, Polygon, FeatureCollection, Point
def index(request):
    df = pd.read_csv('/home/ppc2115/plus/bakchodi/file.csv')
    #basic Cleaning
    cols = ['x', 'y', 'unique_squirrel_id', 'shift', 'date', 'age',
        'primary_fur_color', 'location', 'specific_location', 'running', 'chasing',
        'climbing', 'eating', 'foraging', 'other_activities', 'kuks', 'quaas', 'moans',
        'tail_flags', 'tail_twitches', 'approaches', 'indifferent', 'runs_from']
    df = df[cols]
    df['age'].fillna(0, inplace = True)
    df['date'].fillna(0, inplace = True)
    df['primary_fur_color'].fillna('gray', inplace = True)
    df['location'].fillna('not known', inplace = True)
    df['specific_location'].fillna('not known', inplace = True)
    df['other_activities'].fillna('not known', inplace = True)
    df['foraging'].fillna('not known', inplace = True)
    x_lis = df['x'].tolist()
    y_lis = df['y'].tolist()
    zone_table = [[x,y] for x,y in zip(x_lis, y_lis)]
    coordinate_lis = [Point(i) for i in zone_table]
    prop_lis = df.to_dict(orient = 'records')
    geometry_lis = [Feature(geometry = coordinate_lis[i], properties = prop_lis[i] )
            for i in range(len(coordinate_lis))]
    geo_json = FeatureCollection(geometry_lis)
    df_wt = df[['x','y']]
    m = folium.Map(location = [40.7829, -73.9654], zoom_start = 15)
    m.choropleth(geo_data = geo_json, data = df_wt, columns = ['x', 'y'],
            key_on = 'feature.properties.x', fill_color = 'YlGn',
            fill_opacity = 0.7, line_opacity = 0.2)
    return HttpResponse(m.get_root().render())

print("hi")


#Create your views here.
