from django.urls import path, include
from sys_modulo import views

urlpatterns = [
    path('', views.index, name="modulo"), # se não existir ocorre erro
    path('edit/', views.edit, name='modulo_insert'),
    path('edit/<int:pk>', views.edit, name='modulo_update'),
    path('delete/<int:pk>', views.delete, name='modulo_delete'),
]