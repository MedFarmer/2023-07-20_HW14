from django.contrib import admin
from django.urls import path, re_path
from .views import index

app_name = 'app4'
urlpatterns = [
    path('', index, name='index'),    
]
