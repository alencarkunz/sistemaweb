from sys_usuario.models import Usuario

def validar_sessao(request):
    #validar sessão do usuario - apenas um login
    row_usuario = Usuario.objects.get(pk=request.user.id)
    return row_usuario.check_session(request)