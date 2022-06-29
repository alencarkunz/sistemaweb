from django.db import models

class DashbordAtendimento(models.Model):
    
    class Meta:
        db_table = 'dashbord_atendimento' # definir nome da tabela
        ordering = ['DAD_ORD'] # definir para não dar warning do pagination no console 

    DAD_ID = models.AutoField(primary_key=True, verbose_name="Código")
    DAD_NOM = models.CharField(max_length=100, verbose_name="Nome")
    DAD_ORD = models.SmallIntegerField(verbose_name="Ordem", null=True)
    DAD_STA = models.BooleanField(verbose_name="Status", default=1)
    
    def __str__(self):
        return self.MEN_NOM
    
    def get_status(AbstractUser):
        returno = 'Inativo'
        if AbstractUser.MEN_STA == 1:
            returno = 'Ativo'
        return returno
    




