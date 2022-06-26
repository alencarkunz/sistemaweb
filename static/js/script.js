var ak_modal = ''

$(document).ready(function(){

    $('.m_i_exit').click(function(){
        var msg = 'Deseja sair do sistema?'; 
        try { ak_modal.hide(); } catch (e) { }
        $('body').append('<div class="modal modal-sm" id="ak-modal"><div class="modal-dialog"><div class="modal-content"><div class="modal-body">'+msg+'</div><div class="modal-footer"><button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Não</button><button type="button" class="btn btn-primary btn-m_i_exit">Sim</button></div></div></div></div>');
        ak_modal = new bootstrap.Modal(document.getElementById('ak-modal'),{ backdrop : 'static' })
        ak_modal.show()   
    });
    $(document).on('click', '.btn-m_i_exit', function() {
        $('#gw-modal-msg').modal('hide'); 
        location = '/sistema/logout'; 
    });

    // desativa itens do campo select que está como leitura
    $('select[readonly=readonly] option:not(:selected)').prop('disabled', true);

    $("form").submit(function(){ modal(); if($(this).attr('name') != 'form_edt'){ setTimeout(function(){ remove_modal(); }, 2000); } });

    setTimeout(tooltip(), 1000);

    //setTimeout(function(){ $('#ak-messages').hide( 500, function() { $( this ).remove(); }) }, 3000); 
    setTimeout(function(){ $('#ak-messages').hide('slow') }, 3000); 
});

function tooltip(){
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        //return new bootstrap.Tooltip(tooltipTriggerEl)
        return new bootstrap.Tooltip(tooltipTriggerEl, {
            delay: { "show": 100, "hide": 200 }
        })
    })
}

function modal(tempo,texto){
    if(tempo == '' || tempo === undefined) tempo = 'mostrar';
    if(texto == '' || texto === undefined) texto = 'Processando...';
    try { ak_modal.hide(); } catch (e) { }
    $('body').append('<div class="modal modal-sm" id="ak-modal"><div class="modal-dialog"><div class="modal-content"><div class="modal-body"><div class="loading"><img src="/static/images/loader.gif" /> '+texto+'</div></div></div></div></div>');
    ak_modal = new bootstrap.Modal(document.getElementById('ak-modal'), { backdrop : 'static' })
    ak_modal.show()
    if(tempo == 'mostrar') setTimeout(function(){ remove_modal(); },90000);
}
function remove_modal(){
    ak_modal.hide()
}

function modal_msg(msg,titulo){
    var header = '';
    if(titulo == '' || titulo === undefined) titulo = ' ';
    try { ak_modal.hide(); } catch (e) { }
    if(titulo.length > 0) header = '<div class="modal-header"><h5 class="modal-title" id="staticBackdropLabel">'+titulo+'</h5><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button></div>';
    $('body').append('<div class="modal modal-sm" id="ak-modal"><div class="modal-dialog"><div class="modal-content">'+header+'<div class="modal-body">'+msg+'</div></div></div></div>');
    ak_modal = new bootstrap.Modal(document.getElementById('ak-modal'))
    ak_modal.show()
    setTimeout(function(){ remove_modal(); },90000);  
}
function remove_modal_msg(){
    ak_modal.hide();
}