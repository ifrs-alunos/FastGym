from django import forms
from .. import models

class PersonalProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ('owner','academias')
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'}),
        }
        labels = {
            'telefone': 'Telefone',
            'rg': 'RG',
            'cpf': 'CPF',
            'nascimento':'Data de Nascimento (ano-mes-dia)',
            'endereco':'Endereço',
            'sexo':'Sexo',
        }
