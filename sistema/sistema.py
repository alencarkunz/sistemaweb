#from django.db import connection
from django.urls import resolve


def define():
    par = {
        #sistema
        'ano_ini_sis' : '2022',
        'sis_modulo' : 'sistema',
        'sis_titulo' : 'Sistema Web',
        'sis_titulo_login' : '',

        'sis_email_admin' : 'alenkar.k@gmail.com',
        'sis_email_nome': 'Sistema Web',
        
        'num_pag' : 25,
        
        # Mensagens form
        'form_save' : 'Registro gravado com sucesso!',
           
        'frm_btn_salvar' : 'Salvar',
        'frm_btn_cancelar' :  'Cancelar',
        
        # Mensagens geral
        'msg_sucesso_gravar_login' : 'Suas alterações foram realizadas com sucesso!',
        'msg_sair_sistema' : 'Deseja sair do sistema?',
        'msg_erro_delete' : 'O registro não pode ser excluído!',
        'msg_erro_valida_login' : 'Login já utilizado!',
        'msg_erro_valida_email' : 'E-mail já utilizado!',  
    }

    return par

def get_parametros_app(request,app_name = None):
    if app_name is None:
        app_name = resolve(request.path).route.split('/')[0]
    mod = request.session['modelo_app'][app_name]
    par_app = { 
        'modulo'    : mod,
        'app_name'  : app_name,
        'app_title' : mod['nome_pagina'] if mod['nome_pagina'] else mod['titulo'],
        'app_insert': mod['modelo']+'_insert', # url route
        'app_update': mod['modelo']+'_update', # url route
        'app_delete': mod['modelo']+'_delete', # url route
        'html_list' : mod['modelo']+'/list.html', # render mod['modelo']+'_list.html'
        'html_form' : mod['modelo']+'/form.html', # render mod['modelo']+'_form.html'
        'url_index' : mod['modelo'], # redirect
    }
    return par_app

# def get_modulo(modelo):
#     cursor = connection.cursor()
#     query = """ select m.MOD_NOM, m.MOD_NUMPAG
#                 from MODULOS m 
#                 where m.MOD_MDL = %s """
#     row = cursor.execute(query, [modelo]).fetchone()
#     par = {
#         'modelo' : modelo,
#         'titulo' : row[0],
#         'num_pag' : (row[1] if row[1] > 0 else '25'),
#     }
#     return par