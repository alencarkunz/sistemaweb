from django.contrib import admin
from sys_menu.models import Menu


@admin.register(Menu) # ou admin.site.register(Menu,MenuAdmin)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('MEN_ID', 'MEN_NOM', 'MEN_ORD', 'MEN_STA')
    #list_display = [field.name for field in Menu._meta.get_fields()] # lista todas colunas
    search_fields = ['MEN_NOM']
    list_display_links = ['MEN_ID','MEN_NOM']
    ordering = ('MEN_ORD','MEN_NOM')
