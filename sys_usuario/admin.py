from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import Usuario
from .forms import UsuarioChangeForm, UsuarioCreationForm


##admin.site.register(Usuario,auth_admin.UserAdmin)

@admin.register(Usuario)
class UsuarioAdmin(auth_admin.UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    model = Usuario
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        #("Informações Pessoais", {"fields": ("USU_DES",)}),
        #("Permissão", {"fields": ("PER_ID",)}),
        ("session_key", {"fields": ("session_key",)}),
    )