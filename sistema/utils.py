
def get_parm_gp(request):

    if request.method == 'GET':
        rqp = request.GET
    elif request.method == 'POST':
        rqp = request.POST
    
    return rqp

def get_param_to_url(request):

    if request.method == 'GET':
        rqp = request.GET
    elif request.method == 'POST':
        rqp = request.POST

    get_url = ''
    for pgp in rqp:
        if len(rqp.get(pgp,'').rstrip()) > 0 and pgp != 'csrfmiddlewaretoken' and pgp != 'page':
            get_url += '&'+pgp+'='+rqp.get(pgp,'').rstrip()
    
    return get_url