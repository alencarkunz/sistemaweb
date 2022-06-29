from django.contrib import admin
from django.urls import path, include
from dashbord_atendimento import views

urlpatterns = [
    path('', views.index, name='dashbord_atendimento'), # index é uma função então chama views.index
]