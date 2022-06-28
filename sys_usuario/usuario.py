from sys_usuario.models import Usuario

def validar_sessao(request):
    #validar sessão do usuario - apenas um login
    row_usuario = Usuario.objects.get(pk=request.user.id)
    return row_usuario.check_session(request)


def get_view_permissao(app_name, get_group_permissions):
    # retorn permissões do modulo app
    # modulo = 'menu'
    # get_group_permissions = request.user.get_group_permissions()
    perm = {}
 
    modulo = 'sys_'+app_name #sys_usuario.views

    if (modulo+'.view_'+app_name in list(get_group_permissions)): # 'sys_usuario.view_usuario' in
        perm['view'] = True
    else:
        perm['view'] = False
    
    if (modulo+'.add_'+app_name in list(get_group_permissions)): # 'sys_usuario.add_usuario' in
        perm['add'] = True
    else:
        perm['add'] = False
    
    if (modulo+'.change_'+app_name in list(get_group_permissions)): # 'sys_usuario.change_usuario' in
        perm['change'] = True
    else:
        perm['change'] = False
    
    if (modulo+'.delete_'+app_name in list(get_group_permissions)): # 'sys_usuario.delete_usuario' in
        perm['delete'] = True
    else:
        perm['delete'] = False

    return perm