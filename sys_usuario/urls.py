from django.urls import path, include
from sys_usuario import views

urlpatterns = [
    path('', views.index, name="usuario"), # se não existir ocorre erro
    path('edit/', views.edit, name='usuario_insert'),
    path('edit/<int:pk>', views.edit, name='usuario_update'),
    path('delete/<int:pk>', views.delete, name='usuario_delete'),
    path('meusdados/<int:pk>', views.meusdados, name='meusdados'),
    path('password/<int:pk>', views.password, name='password_update'),
    path('password/<int:pk>/<int:btn_cancel_inative>', views.password, name='meu_password_update'),
]