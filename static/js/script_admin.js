$(document).ready(function(){

   var elementos = 'input,select,textarea,a,button';
   //$(document).on("dblclick",elementos,function(){
   $(document).on("keyup",elementos,function(e){
        if(e.which == 119){ // ctrl + f8
            var tip = '';

            $(this).each(function(index,value) {
                if(value == '[object HTMLInputElement]') tip = 'input';
                else if(value == '[object HTMLSelectElement]') tip = 'select';
                else if(value == '[object HTMLTextAreaElement]') tip = 'textarea';
            });

            var text = '*** Atributos ***';
            text += '\n' + 'id: ' + $(this).attr('name');
            text += '\n' + 'name: ' + $(this).attr('name');

            if(tip == 'input') text += '\n' + 'type: ' + $(this).attr('type');
            
            text += '\n' + 'class: ' + $(this).attr('class');
            text += '\n' + 'value: ' + $(this).val();
            //text += '\n' + 'text: ' + $(this).text(); 
            text += '\n' + 'html: ' + $(this).html();

            alert(text);
        }
    });
    
    
});
