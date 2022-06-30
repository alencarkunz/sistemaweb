from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required

import sistema.sistema as _sistema
import sys_usuario.usuario as _usuario

_app_name = 'dashbordatendimento'
## parametro para o app
def init(request):
    _par_app = _sistema.get_parametros_app(request)
    _render = _usuario.validar_sessao(request)
    _user_perm = _usuario.get_view_permissao(_app_name,request.user.get_group_permissions())
    
    _par_app['obj'] = ''
    _par_app['obj_form'] = ''
    
    return _par_app, _user_perm, _render

@login_required(login_url='login')
def index(request):
    par_app, user_perm, _render = init(request)

    return render(request, 'dashbord_atendimento/index.html', context = { })