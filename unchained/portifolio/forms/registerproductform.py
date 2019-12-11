from django import forms
from ..models import Product

class RegisterProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('academia', 'compradores')

        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.NumberInput(attrs={'class':'form-control', 'step':'0.01'}),
            'quantidade':forms.NumberInput(attrs={'class':'form-control'}),
            'descricao':forms.Textarea(attrs={'class':'form-control'})
        }

        fields = {
            'nome':'Nome do produto',
            'valor': 'Valor do produto',
            'quantidade': 'Quantidade disponível',
            'descricao': 'Descrição'
        }