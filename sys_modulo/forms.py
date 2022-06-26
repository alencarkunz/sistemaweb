from django import forms 
from django.contrib.auth import forms as forms_auth

from .models import Modulo


class ModuloForm(forms.ModelForm):  
    #text_label = Modulo._meta.get_field('MOD_NOM').verbose_name # pega descrição nome field do modelo
    #MOD_NOM = forms.CharField(label=text_label, widget=forms.TextInput(attrs={'class': 'my_class'}) ) # definir atributo do elemento do form

    class Meta:  
        model = Modulo  
        fields = "__all__" # todos os campos