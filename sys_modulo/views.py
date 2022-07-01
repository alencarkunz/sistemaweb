from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import JsonResponse
from django.contrib import messages
from sys_acessos.models import Acessos

from sys_modulo.models import Modulo
from sys_modulo.forms import ModuloForm
import sistema.sistema as _sistema
import sys_usuario.usuario as _usuario

_app_name = 'modulo'
## parametro para o app
def init(request):
    _par_app = _sistema.get_parametros_app(request)
    _render = _usuario.validar_sessao(request)
    _user_perm = _usuario.get_view_permissao(_app_name,request.user.get_group_permissions())
    
    _par_app['obj'] = Modulo
    _par_app['obj_form'] = ModuloForm
    
    #registros de acessos
    Acessos.set_acessos(request)

    return _par_app, _user_perm, _render

@login_required(login_url='login')
def index(request):
    par_app, user_perm, _render = init(request)

    fil_des = request.POST.get("fil_des",'').rstrip()

    rows = par_app['obj'].objects  

    if len(fil_des) > 0: 
        rows = rows.filter(MOD_NOM__contains=fil_des)
    else:
        rows = rows.all()

    rows = rows.order_by('MEN_ID__MEN_ORD','MOD_ORD') # MEN_ID__MEN_ORD join do Menu

    # paginação
    paginator = Paginator(rows, par_app['modulo']['num_pag']) 
    page = int(request.GET.get('page', '1'))
    rows = paginator.get_page(page)

    context = { 'rows': rows, 'fil_des' : fil_des, 'par_app' : par_app, 'user_perm' : user_perm }

    if _render:
        return render(request, par_app['html_list'], context=context)
    else: 
        return redirect('login')     

@login_required(login_url='login') # sem login, retorna para login
@permission_required(('sys_'+_app_name+'.add_'+_app_name,'sys_'+_app_name+'.change_'+_app_name),login_url='index') # (sys_menu.add_menu,sys_menu.change_menu) sem permissão, retorna para index
def edit(request, pk=0):
    par_app, user_perm, _render = init(request)
    
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
        'user_perm' : user_perm,
    }

    return render(request, par_app['html_form'], context=context)

@login_required(login_url='login')
@permission_required('sys_'+_app_name+'.delete_'+_app_name,login_url='index') # (sys_menu.delete_menu) sem permissão, retorna para index
def delete(request, pk=0):  
    par_app = init(request)[0]
    row = par_app['obj'].objects.get(MOD_ID=pk).delete() if pk > 0 else '' 
   
    if row is not None:
        ok = True
        msg = '' 
    else:
        ok = True
        msg = _sistema.define()['msg_erro_delete']
        
    return JsonResponse({'ok' : ok, 'msg' : msg})
    #return redirect(par_app['url_index']) 
