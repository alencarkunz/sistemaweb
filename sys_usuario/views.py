from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib import messages
from django.db import connection
from django.db.models import Q

from sys_usuario.forms import UsuarioForm, UsuarioInsertForm, PasswordForm, UsuarioMeusDadosForm
from sys_usuario.models import Usuario
import sistema.sistema as _sistema
import sys_usuario.usuario as _usuario

_app_name = 'usuario'
## parametro para o app
def init(request):
    _par_app = _sistema.get_parametros_app(request)
    _render = _usuario.validar_sessao(request)
    _user_perm = _usuario.get_view_permissao(_app_name,request.user.get_group_permissions())
    
    _par_app['obj'] = Usuario
    _par_app['obj_form'] = UsuarioForm
    
    return _par_app, _user_perm, _render

@login_required(login_url='login')
def index(request):
    par_app, user_perm, _render = init(request)
    
    fil_des = request.POST.get("fil_des",'').rstrip()
    
    rows = Usuario.objects  

    # regra para usuário  diferente de 1 - adm master
    if request.user.id > 1: 
        rows = rows.filter(id__gt=1) # > 1
        rows = rows.filter(Q(id__exact=request.user.id) | Q(groups__gt=1)) ## groups join com USUARIOS_groups 

    if len(fil_des) > 0: 
        rows = rows.filter(first_name__iexact=fil_des)
    else:
        rows = rows.all()

    rows = rows.order_by('username')
    
    # paginação
    paginator = Paginator(rows, par_app['modulo']['num_pag'])
    page = int(request.GET.get('page', '1'))
    rows = paginator.get_page(page)

    context = { 'rows': rows, 'fil_des' : fil_des, 'par_app' : par_app, 'user_perm' : user_perm }

    if _render:
        return render(request, 'usuario_list.html', context=context)
    else: 
        return redirect('login')

@login_required(login_url='login') # sem login, retorna para login
@permission_required(('sys_'+_app_name+'.add_'+_app_name,'sys_'+_app_name+'.change_'+_app_name),login_url='index') # (sys_menu.add_menu,sys_menu.change_menu) sem permissão, retorna para index
def edit(request, pk=0):
    par_app, user_perm, _render = init(request)

    obj = par_app['obj'] # model
    obj_form = par_app['obj_form'] # for

    row = obj.objects.get(id=pk) if pk > 0 else ''
    if request.method == "POST":
        if pk > 0:
            form = obj_form(request.POST, instance = row)
        else:
            form = UsuarioInsertForm(request.POST)

        if form.is_valid(): 
            if pk > 0:
                row = form.save()
                row.group_id = request.POST['group_id'] # atualiza grupo
                row.save()
            else: 
                row = form.save()
                row.password = make_password(row.password) ## or form.cleaned_data['password']
                row.group_id = request.POST['group_id'] # atualiza grupo
                row.save()
            
            # gravar o grupo do usuário no relacionamento USUARIOS_groups
            if request.POST['group_id'] is not None:
                cursor = connection.cursor()
                
                query = "DELETE FROM USUARIOS_groups WHERE usuario_id = %s"
                cursor.execute(query, [row.pk]).fetchone()

                query = "INSERT INTO USUARIOS_groups(usuario_id, group_id) VALUES( %s , %s )"
                cursor.execute(query, [row.pk, request.POST['group_id']])
                        

            messages.success(request, _sistema.define()['form_save'])
            return redirect(par_app['url_index'])
    else:
        form = obj_form(instance = row) if pk > 0 else UsuarioInsertForm()

    #grupos
    cursor = connection.cursor()
    # não mostrar usuário 1 adm master
    where = ''
    if request.user.group_id > 1:
        where = 'where id > 1'

    query = "select ag.id, ag.name from auth_group ag "+where+" "   
    auth_group = cursor.execute(query).fetchall()

    #grupo do usuario
    cursor = connection.cursor()
    query = "select ug.group_id as id from USUARIOS_groups ug where ug.usuario_id = %s"
    result = cursor.execute(query, [pk]).fetchone()
    auth_group_set = result[0] if result is not None else '' 
 
    context = {
        'row': row,
        'form' : form,
        'btn_cancel_inative' : 0,
        'auth_group' : auth_group,
        'auth_group_set' : auth_group_set,
        'user_perm' : user_perm,
    }

    return render(request, par_app['html_form'], context=context)

"""
@login_required(login_url='login')
def delete(request, pk=0):  
    # deletar o grupo do usuario
    cursor = connection.cursor()
    query = "delete from USUARIOS_groups where usuario_id = %s"
    cursor.execute(query, [pk]).fetchone()
    
    row = Usuario.objects.get(id=pk).delete() if pk > 0 else ''
    return redirect('usuario')"""

@login_required(login_url='login')
@permission_required('sys_'+_app_name+'.delete_'+_app_name,login_url='index') # (sys_menu.delete_menu) sem permissão, retorna para index
def delete(request, pk=0):  
    par_app = init(request)[0]
    
    # deletar o grupo do usuario
    cursor = connection.cursor()
    query = "delete from USUARIOS_groups where usuario_id = %s"
    cursor.execute(query, [pk]).fetchone()
    
    row = par_app['obj'].objects.get(id=pk).delete() if pk > 0 else '' 
   
    if row is not None:
        ok = True
        msg = '' 
    else:
        ok = True
        msg = _sistema.define()['msg_erro_delete']
        
    return JsonResponse({'ok' : ok, 'msg' : msg})
    #return redirect(par_app['url_index']) 




@login_required(login_url='login') 
def password(request, pk, btn_cancel_inative=0):
    par_app = init(request)[0]
    row = par_app['obj'].objects.get(id=pk)
    if request.method == "POST":
        form = PasswordForm(request.POST, instance = row)
        if form.is_valid(): 
            # atualizar a senha do usuário # criar hash de senha print(make_password(row.password))
            row.set_password(row.password)
            form.save()
            if btn_cancel_inative:
                return redirect('index')    
            else:
                return redirect('usuario')
                
    else:
        form = PasswordForm()

    context = {
        'row': row,
        'form' : form,
        'btn_cancel_inative' : btn_cancel_inative,
    }

    return render(request, 'password.html', context=context)


@login_required(login_url='login') 
def meusdados(request, pk=0):
    par_app = init(request)[0]
    row = par_app['obj'].objects.get(id=pk)

    if request.method == "POST":
        form = UsuarioMeusDadosForm(request.POST, instance = row)
        if form.is_valid():
            form.save()
            #return redirect('index')
    else:
        form = UsuarioMeusDadosForm(instance = row)

    context = {
        'row': row,
        'form' : form,
        'btn_cancel_inative': 1,
        'per_id_inative': 1,
        'status_inative': 1,
    }

    return render(request, par_app['html_form'], context=context)
