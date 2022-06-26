from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib import messages

from sys_modulo.models import Modulo
from sys_modulo.forms import ModuloForm
import sistema.sistema as _sistema
import sys_usuario.usuario as _usuario

## parametro para o app
def get_parametros_app():
    app_name = 'modulo'
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
        'obj'       : Modulo, # model
        'obj_form'  : ModuloForm, # form
    }
    return par_app

@login_required(login_url='login')
def index(request):
    _render = _usuario.validar_sessao(request)
    par_app = get_parametros_app()
    fil_des = request.POST.get("fil_des",'').rstrip()

    rows = par_app['obj'].objects  

    if len(fil_des) > 0: 
        rows = rows.filter(MOD_NOM__iexact=fil_des)
    else:
        rows = rows.all()

    # paginação
    paginator = Paginator(rows, par_app['modulo']['num_pag']) 
    page = int(request.GET.get('page', '1'))
    rows = paginator.get_page(page)

    context = { 'rows': rows, 'fil_des' : fil_des, 'par_app' : par_app }

    if _render:
        return render(request, par_app['html_list'], context=context)
    else: 
        return redirect('login')     

@login_required(login_url='login') 
#@permission_required('usuarios.add_usuario',login_url='index') # se sem permissão, retorna para tela de login
def edit(request, pk=0):
    par_app = get_parametros_app()
    
    obj = par_app['obj'] # model
    obj_form = par_app['obj_form'] # form

    row = obj.objects.get(MOD_ID=pk) if pk > 0 else '' # queryset
    
    if request.method == "POST":
    
        form = obj_form(request.POST, instance = row) if pk > 0 else obj_form(request.POST)

        if form.is_valid(): 
            form.save()   
            messages.success(request, _sistema.define()['form_save'])
            return redirect(par_app['url_index'])
    else:
        form = obj_form(instance = row) if pk > 0 else obj_form()

    context = {
        'row': row,
        'form' : form,
        'par_app' : par_app,
    }

    return render(request, par_app['html_form'], context=context)

@login_required(login_url='login')
def delete(request, pk=0):  
    par_app = get_parametros_app()
    row = par_app['obj'].objects.get(MOD_ID=pk).delete() if pk > 0 else ''
    return redirect(par_app['url_index']) 
