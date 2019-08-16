from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list,),
    url(r'^fecha/$', views.fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', views.horas_adelante),
    ]