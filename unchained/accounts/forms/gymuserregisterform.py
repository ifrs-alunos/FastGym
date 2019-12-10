from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

class MyGymUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyGymUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].help_text = ""

        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].help_text = ""

    class Meta:
        model = User
        fields = ('email', 'first_name')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name' : 'Nome da Empresa',
            'email' : 'Email',
        }

    def clean(self):
        cleaned_data = super().clean()
        if User.objects.filter(email=cleaned_data.get('email')).exists():
            self.add_error('email', ValidationError("Email já cadastrado"))
        return cleaned_data

    def save(self, commit=True):
        user = super(MyGymUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user

