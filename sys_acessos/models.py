from django.db import models
from django.utils.timezone import datetime

from sys_usuario.models import Usuario


class Acessos(models.Model):

    class Meta:
        db_table = 'ACESSO_PAGINAS' # definir nome da tabela

    ACE_ID = models.AutoField(primary_key=True, verbose_name="Código")
    ACE_URL = models.CharField(max_length=150, verbose_name="URL")
    id_usuario = models.IntegerField(verbose_name="Usuário")
    ACE_DATHOR = models.DateTimeField(verbose_name="Data e Hora", auto_now_add=True)
    ACE_PST = models.TextField(verbose_name="Post")
    ACE_IP = models.CharField(max_length=20, verbose_name="IP")

    def get_usuario(self):
        obj = Usuario.objects.get(pk=self.id_usuario)
        return obj.username 

    def set_acessos(request):
        
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        obj = Acessos(
            ACE_URL = request.path, 
            id_usuario = request.user.id, 
            ACE_PST = request.POST.dict(),
            ACE_IP = ip,
        )

        return obj.save()
