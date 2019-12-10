from django import forms
from .. import models

class GymProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = models.Gym
        exclude = ('owner','associados')
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'telefone': 'Telefone',
            'cnpj': 'CNPJ',
            'endereco':'Endereço',
        }
