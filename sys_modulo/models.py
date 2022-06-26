from django.db import models
from sys_menu.models import Menu 
from django.db import connection

class Modulo(models.Model):
    
    class Meta:
        db_table = 'MODULOS' # definir nome da tabela
        ordering = ['MOD_ORD'] # definir para não dar warning do pagination no console 

    MOD_ID = models.AutoField(primary_key=True, verbose_name="Código")
    MOD_NOM = models.CharField(max_length=100, verbose_name="Nome")

    cursor = connection.cursor()
    query = 'select dct.model, dct.model app_label  from django_content_type dct order by dct.model' ## dct.app_label
    list_choices = cursor.execute(query).fetchall()

    MOD_MDL = models.CharField(max_length=100, choices=list_choices,verbose_name="Modelo")

    MEN_ID = models.ForeignKey(Menu, db_column='MEN_ID', on_delete=models.PROTECT, verbose_name="Menu")
    MOD_NUMPAG = models.SmallIntegerField(verbose_name="Paginas", default=25)
    MOD_ORD = models.SmallIntegerField(verbose_name="Ordem")
    MOD_STAMEN = models.SmallIntegerField(verbose_name="Status Menu", default=1)
    MOD_STA = models.BooleanField(verbose_name="Status", default=1)
    
    
    def __str__(self):
        return self.MOD_NOM
    
    def get_status(AbstractUser):
        returno = 'Inativo'
        if AbstractUser.MOD_STA == 1:
            returno = 'Ativo'
        return returno
