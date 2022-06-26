from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db import connection

from sys_usuario.forms import UsuarioForm, UsuarioInsertForm, PasswordForm, UsuarioMeusDadosForm
from sys_usuario.models import Usuario
import sistema.sistema as _sistema
import sys_usuario.usuario as _usuario

## parametro para o app
def get_parametros_app():
    app_name = 'usuario'
    mod = _sistema.get_modulo(app_name)
    app_nome = mod['modelo']
    par_app = { 
        'modulo'    : mod,
        'app_title' : mod['titulo'],
        'app_insert': mod['modelo']+'_insert', # url route
        'app_update': mod['modelo']+'_update', # url route
        'app_delete': mod['modelo']+'_delete', # url route
        'html_list' : mod['modelo']+'_list.html', # render
        'html_form' : mod['modelo']+'_form.html', # render
        'url_index' : mod['modelo'], # redirect
        'obj'       : Usuario, # model
        'obj_form'  : UsuarioForm, # form
    }
    return par_app

@login_required(login_url='login')
def index(request):
    _render = _usuario.validar_sessao(request)
    par_app = get_parametros_app()
    fil_des = request.POST.get("fil_des",'').rstrip()
    
    rows = Usuario.objects  

    if len(fil_des) > 0: 
        rows = rows.filter(first_name__iexact=fil_des)
    else:
        rows = rows.all()

    # paginação
    paginator = Paginator(rows, par_app['modulo']['num_pag'])
    page = int(request.GET.get('page', '1'))
    rows = paginator.get_page(page)

    context = { 'rows': rows, 'fil_des' : fil_des }

    if _render:
        return render(request, 'usuario_list.html', context=context)
    else: 
        return redirect('login') 

@login_required(login_url='login') 
#@permission_required('usuario.add_usuario',login_url='index') # se sem permissão, retorna para tela de login
def edit(request, pk=0):
    par_app = get_parametros_app()
    row = par_app['obj'].objects.get(id=pk) if pk > 0 else ''
    if request.method == "POST":
        if pk > 0:
            form = UsuarioForm(request.POST, instance = row)
        else:
            form = UsuarioInsertForm(request.POST)

        if form.is_valid(): 
            if pk > 0:
                row = form.save()
            else: 
                row = form.save()
                row.password = make_password(row.password) ## or form.cleaned_data['password']
                row.save()
            
            # gravar o grupo do usuário
            if request.POST['auth_group'] is not None:
                cursor = connection.cursor()
                
                query = "DELETE FROM USUARIOS_groups WHERE usuario_id = %s"
                cursor.execute(query, [row.pk]).fetchone()

                query = "INSERT INTO USUARIOS_groups(usuario_id, group_id) VALUES( %s , %s )"
                cursor.execute(query, [row.pk, request.POST['auth_group']])
                        

            messages.success(request, _sistema.define()['form_save'])
            return redirect(par_app['url_index'])
    else:
        form = UsuarioForm(instance = row) if pk > 0 else UsuarioInsertForm()

    #grupos
    cursor = connection.cursor()
    query = "select ag.id, ag.name from auth_group ag order by 1"
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
        'auth_group_set' : auth_group_set
    }

    return render(request, par_app['html_form'], context=context)

@login_required(login_url='login')
def delete(request, pk=0):  
    # deletar o grupo do usuario
    cursor = connection.cursor()
    query = "delete from USUARIOS_groups where usuario_id = %s"
    cursor.execute(query, [pk]).fetchone()
    
    row = Usuario.objects.get(id=pk).delete() if pk > 0 else ''
    return redirect('usuario') 

@login_required(login_url='login') 
#@permission_required('usuario.add_usuario',login_url='index') # se sem permissão, retorna para tela de login
def password(request, pk, btn_cancel_inative=0):
    row = Usuario.objects.get(id=pk)
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
#@permission_required('usuario.add_usuario',login_url='index') # se sem permissão, retorna para tela de login
def meusdados(request, pk=0):
    
    row = Usuario.objects.get(id=pk)

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

    return render(request, 'usuario_form.html', context=context)
