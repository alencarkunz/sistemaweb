from django.contrib import admin
from sys_modulo.models import Modulo

#admin.site.register(Modulo,ModuloAdmin)
@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Modulo._meta.get_fields()] # lista todas colunas
    search_fields = ['MOD_NOM']
    list_display_links = ['MOD_ID','MOD_NOM']
    ordering = ('MOD_ORD','MOD_NOM')
