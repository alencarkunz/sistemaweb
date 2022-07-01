from django.db import models
from sys_menu.models import Menu 
from django.db import connection

class Modulo(models.Model):
    
    class Meta:
        db_table = 'MODULOS' # definir nome da tabela
        ordering = ['MOD_ORD'] # definir para não dar warning do pagination no console 

    MOD_ID = models.AutoField(primary_key=True, verbose_name="Código")
    MOD_NOM = models.CharField(max_length=100, verbose_name="Nome")
    MOD_NOMPAG = models.CharField(max_length=100, verbose_name="Título Página")

    cursor = connection.cursor() 
    query = 'select dct.model, dct.model app_label' ## dct.app_label
    query += ' from django_content_type dct'
    query += ' where dct.model <> "contenttype" and dct.model <> "logentry"'
    query += ' order by dct.model'
    list_choices = cursor.execute(query).fetchall()

    MOD_MDL = models.CharField(max_length=100, choices=list_choices,verbose_name="Modelo")
    MOD_MDLDNM = models.CharField(max_length=100,verbose_name="Modelo Dinâmico", blank=True, null=True)

    MEN_ID = models.ForeignKey(Menu, db_column='MEN_ID', on_delete=models.PROTECT, verbose_name="Menu")
    MOD_NUMPAG = models.SmallIntegerField(verbose_name="Paginas", default=25)
    MOD_ORD = models.SmallIntegerField(verbose_name="Ordem")
    MOD_STAMEN = models.BooleanField(verbose_name="Status Menu", default=1)
    MOD_STA = models.BooleanField(verbose_name="Status", default=1)
    
    
    def __str__(self):
        return self.MOD_NOM
    
    def get_status(AbstractUser):
        retorno = 'Inativo'
        if AbstractUser.MOD_STA == 1:
            retorno = 'Ativo'
        return retorno
