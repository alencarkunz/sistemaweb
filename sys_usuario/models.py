from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import messages




# usuário padrão django personalizado
class Usuario(AbstractUser): 
    #USU_DES = models.TextField(blank=True)
    #PER_ID = models.ForeignKey(Permissao, db_column='PER_ID', on_delete=models.PROTECT, verbose_name="Permissão")
    session_key = models.CharField(blank=True, max_length=100, verbose_name='session_key')
    group_id = models.IntegerField(verbose_name="Permissão")

    class Meta:
        db_table = 'USUARIOS' # definir nome da tabela
        ordering = ['username'] # definir para não dar warning do pagination no console 
        
    def get_status(AbstractUser):
        returno = 'Inativo'
        if AbstractUser.is_active == True:
            returno = 'Ativo'

        return returno
    
    def get_is_checked(AbstractUser):
        retorno = ''
        if AbstractUser.is_active == True:
            retorno = 'checked'
        return retorno
    
    def get_session_key(AbstractUser):
        return AbstractUser.session_key
    

    def check_session(self,request):
        if self.session_key != request.session._session_key:
            messages.warning(request, "Outra sessão está em uso!" )
            request.session.delete()
            return False
        else:
            return True


    