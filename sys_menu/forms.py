from django import forms 
from django.contrib.auth import forms as forms_auth

from .models import Menu


class MenuForm(forms.ModelForm):  
    #text_label = Modulo._meta.get_field('MEN_NOM').verbose_name # pega descrição nome field do modelo
    #MEN_NOM = forms.CharField(label=text_label, widget=forms.TextInput(attrs={'class': 'my_class'}) ) # definir atributo do elemento do form

    class Meta:  
        model = Menu  
        #fields = ['MEN_NOM','MEN_ORD','MEN_STA']
        fields = "__all__" # todos os campos
        #exclude =['MEN_STA',] #remover field do form

    