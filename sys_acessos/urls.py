from django.urls import path, include
from sys_acessos import views

urlpatterns = [
    path('', views.index, name="acessos"), # se não existir ocorre erro
    path('edit/<int:pk>', views.edit, name='acessos_update'),
]