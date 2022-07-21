from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import JsonResponse
from django.contrib import messages
from django.urls import resolve
from django.db.models import Q

from sys_acessos.models import Acessos
from sys_acessos.forms import AcessosForm
import sistema.sistema as _sistema
import sys_usuario.usuario as _usuario
import sistema.utils as _utils
from datetime import datetime 

_app_name = 'acessos'
## parametro para o app
def init(request):
    _par_app = _sistema.get_parametros_app(request)
    _render = _usuario.validar_sessao(request)
    _user_perm = _usuario.get_view_permissao(_app_name,request.user.get_group_permissions())
    
    _par_app['obj'] = Acessos
    _par_app['obj_form'] = AcessosForm
    
    return _par_app, _user_perm, _render

@login_required(login_url='login')
def index(request):  
    par_app, user_perm, _render = init(request)
    
    rqp = _utils.get_parm_gp(request)
    
    fil_datini = rqp.get("fil_datini",'').rstrip()
    fil_datfim = rqp.get("fil_datfim",'').rstrip()
    fil_des = rqp.get("fil_des",'').rstrip()
    fil_mtd = rqp.get("fil_mtd",'').rstrip()

    rows = par_app['obj'].objects  

    if len(fil_datini) > 0: 
        _fil_datini = datetime.strptime(fil_datini+' 00:00:00', '%d/%m/%Y %H:%M:%S')
        rows = rows.filter(ACE_DATHOR__gte=_fil_datini)

    if len(fil_datfim) > 0: 
        _fil_datfim = datetime.strptime(fil_datfim+' 23:59:59', '%d/%m/%Y %H:%M:%S')
        rows = rows.filter(ACE_DATHOR__lte=_fil_datfim)

    if len(fil_des) > 0: 
        #rows = rows.filter(ACE_URL__contains=fil_des)
        rows = rows.filter(Q(ACE_URL__contains=fil_des) | Q(ACE_PST__contains=fil_des))  
    
    if len(fil_mtd) > 0: 
        rows = rows.filter(ACE_MTD__contains=fil_mtd)  

    if len(fil_des) <= 0 and len(fil_mtd) <= 0:
        rows = rows.all()

    rows = rows.order_by('-ACE_DATHOR')

    # paginação
    paginator = Paginator(rows, par_app['modulo']['num_pag']) 
    page = int(request.GET.get('page', '1'))
    rows = paginator.get_page(page)
    get_url_pag = _utils.get_param_to_url(request)

    sel_mtd = ('GET','POST')
    
    context = { 
        'rows': rows, 
        'fil_des' : fil_des, 
        'par_app' : par_app, 
        'user_perm' : user_perm, 
        'fil_datini' : fil_datini, 
        'fil_datfim' : fil_datfim,
        'fil_mtd' : fil_mtd, 
        'sel_mtd' : sel_mtd,
        'get_url_pag' : get_url_pag,
    }

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

    row = obj.objects.get(ACE_ID=pk) if pk > 0 else '' # queryset
    
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
        'user_perm' : user_perm 
    }

    return render(request, par_app['html_form'], context=context)
