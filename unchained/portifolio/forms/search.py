from django import forms

class Search(forms.Form):
    text = forms.CharField(label="Digite aqui sua cidade", max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))