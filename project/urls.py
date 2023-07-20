
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls', namespace='app1')),
    path('app2/', include('app2.urls', namespace='app2')),
    re_path(r'^app3/[a-z]$', include('app3.urls', namespace='app3')), # regex inclusion
    re_path(r'^app4/[0-9]$', include('app4.urls', namespace='app4')), # regex inclusion
]
