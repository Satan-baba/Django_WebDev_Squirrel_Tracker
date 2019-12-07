from django.urls import path, re_path
from . import views


urlpatterns = [
        path('', views.index, name = 'index'),
        re_path(r'(\w+)-([A-Za-z]{2})-(\d{4})-(\d{2})', views.second, name = 'second'),
        path('add/', views.add, name = 'add')
]
