from django.db import connection

def define():

    par = {
        'num_pag' : 25,
        'form_save' : 'Registro gravado com sucesso!'
    }

    return par


def get_modulo(modelo):

    cursor = connection.cursor()
    query = """ select m.MOD_NOM, m.MOD_NUMPAG
                from MODULOS m 
                where m.MOD_MDL = %s """
    row = cursor.execute(query, [modelo]).fetchone()
 
    par = {
        'modelo' : modelo,
        'titulo' : row[0],
        'num_pag' : (row[1] if row[1] > 0 else '25'),
    }

    return par