from django.contrib import admin
from django.urls import path
from .views import home, index

app_name = 'app1'
urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
]
