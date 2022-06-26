from django import forms 
from django.contrib.auth import forms as forms_auth

from .models import Usuario


class UsuarioChangeForm(forms_auth.UserChangeForm):
    class Meta(forms_auth.UserChangeForm.Meta):
        model = Usuario


class UsuarioCreationForm(forms_auth.UserCreationForm):
    class Meta(forms_auth.UserCreationForm.Meta):
        model = Usuario


class UsuarioForm(forms.ModelForm):  
    
    class Meta:  
        model = Usuario  
        fields = ['username','first_name','last_name','email','is_active'] ## ,'PER_ID' ,'password',
        #fields = '__all__'
        #exclude =['password',] #remover field do form

class UsuarioInsertForm(forms.ModelForm):  

    class Meta:  
        model = Usuario  
        fields = ['username','first_name','last_name','email','is_active','password']

class PasswordForm(forms.ModelForm):  
    
    text_label = 'Nova Senha' #Usuario._meta.get_field('password').verbose_name # pega descrição nome field do modelo
    password = forms.CharField(label=text_label, widget=forms.TextInput(attrs={'type': 'password'}) ) # definir atributo do elemento do form


    class Meta:  
        model = Usuario  
        fields = ['password',]
        #fields = '__all__'
        #exclude =['password',] #remover field do form

class UsuarioMeusDadosForm(forms.ModelForm):  
        
    class Meta:  
        model = Usuario  
        fields = ['username','first_name','last_name','email']