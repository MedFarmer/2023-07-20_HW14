from django.contrib import admin
from django.urls import path, re_path
from .views import index

app_name = 'app3'
urlpatterns = [
    path('', index, name='index'),    
]
