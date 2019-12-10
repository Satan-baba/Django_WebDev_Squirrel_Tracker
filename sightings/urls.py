from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    #path('stats/', views.stats, name = 'stats'),
    re_path(r'(?P<user_id>[0-9]+[A-Z]-[A-Z]{2}-[0-9]{4}-[0-9]{2})/', views.s_id, name='user_id'),
    path('stats/',views.stats, name='stats'),
    ]


