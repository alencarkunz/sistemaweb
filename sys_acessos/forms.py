from django import forms 
from .models import Acessos

class DateInput(forms.DateInput):
    input_type = 'date'

class AcessosForm(forms.ModelForm):

    ACE_URL = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    id_usuario = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    ACE_DATHOR = forms.DateTimeField(widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S',attrs={'type': 'date','readonly':'readonly'}), input_formats=('%d/%m/%Y %H:%M:%S', ))
    ACE_PST = forms.CharField(widget=forms.Textarea(attrs={'disabled':'true'}))
    ACE_IP = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    ACE_MTD = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    class Meta:  
        model = Acessos  
        fields = "__all__" # todos os campos


