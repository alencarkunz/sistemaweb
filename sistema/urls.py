from django.contrib import admin
from django.urls import path, include
from sistema import views

urlpatterns = [
    path('', views.index, name='index'), # index é uma função então chama views.index
    path('login/', views.loginUsuario, name="login"), #sistema/logar_usuario/
    path('logout/', views.logoutUsuario, name="logout"), #sistema/logar_usuario/
]