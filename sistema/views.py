import json
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.db import connection

from sys_modulo.models import Modulo
from sys_menu.models import Menu
from sys_usuario.models import Usuario
import sistema.sistema as _sistema
import sys_usuario.usuario as _usuario


@login_required(login_url='login') # se não logado, retorna para tela de login
def index(request):
    _render = _usuario.validar_sessao(request)
    
    context = { }

    if _render:
        return render(request, 'index.html', context=context)
    else: 
        return redirect('login') 


def loginUsuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)

            # gravar sessão no usuario
            row_usuario = Usuario.objects.get(pk=request.user.id)
            row_usuario.session_key = request.session._session_key
            row_usuario.save()

            #montar menu e modulos conforme permissões
            cursor = connection.cursor()
            query = """ select 
                            distinct m.MOD_ID, m.MOD_NOM, m.MOD_MDL, m.MEN_ID, me.MEN_NOM, m.MOD_NUMPAG
                        from USUARIOS_groups ug
                            inner join auth_group_permissions agp on ug.group_id  = agp.group_id 
                            inner join auth_permission ap on agp.permission_id = ap.id 
                            inner join django_content_type dct on ap.content_type_id = dct.id 
                            inner join MODULOS m on dct.model = m.MOD_MDL
                            inner join MENU me on me.MEN_ID  = m.MEN_ID
                        where ug.usuario_id = %s
                        and m.MOD_STAMEN = 1 
                        order by me.MEN_ORD, m.MOD_ORD 
                    """
            cursor.execute(query, [request.user.id])
            result = cursor.fetchall()
            #print(result)
            menu_id = 0
            modulo = []
            menu = []
            modulo_app = {}
            for row in result:
                modulo.append({
                    'id' : row[0], 
                    'nome' : row[1],
                    'rot' : row[2],
                    'menu_id' : row[3],
                })

                if menu_id != row[3]:
                    menu_id = row[3]
                    menu.append({ 'id' : menu_id, 'nome' : row[4] })

                modulo_app[row[2]] = {
                    'modelo' : row[2],
                    'titulo' : row[1],
                    'num_pag' : (row[5] if row[5] > 0 else '25'),
                }
                
                    
            request.session['modulo'] = modulo
            request.session['menu'] = menu
            request.session['modelo_app'] = modulo_app

            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        if request.user.is_authenticated: # se logado retorna para index
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    
    context = { 
        'form_login': form_login,
    }

    return render(request, 'login.html', context = context)

def logoutUsuario(request):
    logout(request)
    return redirect('index')
    

