from django.urls import path, include
from sys_menu import views

urlpatterns = [
    path('', views.index, name="menu"), # se não existir ocorre erro
    path('edit/', views.edit, name='menu_insert'),
    path('edit/<int:pk>', views.edit, name='menu_update'),
    path('delete/<int:pk>', views.delete, name='menu_delete'),
]