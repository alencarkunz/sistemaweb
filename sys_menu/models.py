from django.db import models
from django.urls import reverse

class Menu(models.Model):
    
    class Meta:
        db_table = 'MENU' # definir nome da tabela
        ordering = ['MEN_ORD'] # definir para não dar warning do pagination no console 

    MEN_ID = models.AutoField(primary_key=True, verbose_name="Código")
    MEN_NOM = models.CharField(max_length=100, verbose_name="Nome")
    MEN_ORD = models.SmallIntegerField(verbose_name="Ordem", null=True)
    MEN_STA = models.BooleanField(verbose_name="Status", default=1)
    
    def __str__(self):
        return self.MEN_NOM
    
    def get_status(AbstractUser):
        retorno = 'Inativo'
        if AbstractUser.MEN_STA == 1:
            retorno = 'Ativo'
        return retorno
    




